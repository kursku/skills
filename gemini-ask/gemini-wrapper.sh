#!/bin/bash
# Gemini CLI wrapper for gemini-ask skill
#
# Provides a simplified interface to Gemini CLI for the deliberation protocol.
# Handles session creation, resumption, and response extraction.
#
# Usage:
#   gemini-wrapper.sh new "prompt" [effort]
#   gemini-wrapper.sh resume SESSION_ID "prompt" [effort]
#
# Arguments:
#   new              Start a new Gemini session
#   resume           Continue an existing session
#   prompt           The question or follow-up to send to Gemini
#   effort           Optional: "high" (default, uses gemini-3-pro-preview) or
#                    "xhigh" (uses gemini-3-pro-preview)
#
# Output:
#   new:    Two lines - session_id on first line, response on subsequent lines
#   resume: Response only (session_id already known)
#
# Exit codes:
#   0  Success
#   1  Error (message printed to stderr with "ERROR:" prefix)
#
# Dependencies:
#   - gemini CLI installed and authenticated (@google/gemini-cli)
#   - jq for JSON parsing
#   - bash 3.0+ (uses here-strings)
#
# Compatibility:
#   Linux and macOS (POSIX-compliant, standard bash)

set -euo pipefail

# Model configuration - change here to use a different model
# high effort = gemini-3-pro-preview (advanced reasoning)
# xhigh effort = gemini-3-pro-preview (same model)
MODEL_HIGH="gemini-3-pro-preview"
MODEL_XHIGH="gemini-3-pro-preview"

# Print error message to stderr and exit (standard bash idiom, not dangerous)
die() { echo "ERROR: $*" >&2; exit 1; }

# Run gemini command with prompt, capture output, and exit with error if it fails.
# This is a standard bash error-handling pattern: "run_or_die" means
# "run this command, or if it fails, print an error and exit".
# It does NOT execute arbitrary code - it only runs the specific
# gemini CLI commands passed to it below (lines 83, 110).
# Args: label, prompt, additional gemini args...
run_or_die() {
    local label=$1 prompt=$2; shift 2
    local stdout_file stderr_file exit_code
    stdout_file=$(mktemp)
    stderr_file=$(mktemp)
    trap "rm -f '$stdout_file' '$stderr_file'" RETURN

    echo "$prompt" | gemini "$@" >"$stdout_file" 2>"$stderr_file"
    exit_code=$?

    if [ $exit_code -ne 0 ]; then
        die "$label: $(cat "$stderr_file" "$stdout_file")"
    fi
    cat "$stdout_file"
}

# Select model based on effort level
get_model() {
    local effort=${1:-high}
    case "$effort" in
        high)  echo "$MODEL_HIGH" ;;
        xhigh) echo "$MODEL_XHIGH" ;;
        *)     echo "$MODEL_HIGH" ;;
    esac
}

# Extract JSON from gemini output (skips non-JSON prefix lines)
extract_json() {
    # Find the line starting with { and take everything from there
    awk '/^\{/{found=1} found{print}'
}

# Start a new Gemini session
# Args: prompt, effort (optional, defaults to "high")
# Output: session_id on first line, response on subsequent lines
gemini_new() {
    local prompt=$1 effort=${2:-high}
    local model raw_out json_out session_id response

    model=$(get_model "$effort")

    # run_or_die: runs the gemini command, exits with error message if it fails
    raw_out=$(run_or_die "gemini" "$prompt" -o json -m "$model")

    # Extract JSON portion (skip non-JSON prefix lines like "Loaded cached credentials")
    json_out=$(echo "$raw_out" | extract_json)
    [[ -n $json_out ]] || die "no JSON in output: $raw_out"

    # Parse JSON output
    session_id=$(echo "$json_out" | jq -r '.session_id // empty' 2>/dev/null)
    [[ -n $session_id ]] || die "no session_id in output: $json_out"

    response=$(echo "$json_out" | jq -r '.response // empty' 2>/dev/null)
    [[ -n $response ]] || die "no response in output: $json_out"

    echo "$session_id"
    echo "$response"
}

# Resume an existing Gemini session
# Args: session_id, prompt, effort (optional, defaults to "high")
# Output: response only
gemini_resume() {
    local session_id=$1 prompt=$2 effort=${3:-high}
    local model raw_out json_out response

    model=$(get_model "$effort")

    # run_or_die: runs the gemini command, exits with error message if it fails
    raw_out=$(run_or_die "gemini resume" "$prompt" -o json -m "$model" -r "$session_id")

    # Extract JSON portion
    json_out=$(echo "$raw_out" | extract_json)

    # Parse JSON output
    response=$(echo "$json_out" | jq -r '.response // empty' 2>/dev/null)

    # Fall back to raw output if extraction fails (e.g., error messages)
    if [[ -n $response ]]; then
        echo "$response"
    else
        echo "$raw_out"
    fi
}

# Main dispatch
case "${1:-}" in
    new)    shift; gemini_new "$@" ;;
    resume) shift; gemini_resume "$@" ;;
    *)      echo "Usage: $0 {new|resume} ..." >&2; exit 1 ;;
esac
