#!/bin/bash
# Codex CLI wrapper for codex-ask skill
#
# Provides a simplified interface to Codex CLI for the deliberation protocol.
# Handles session creation, resumption, and response extraction.
#
# Usage:
#   codex-wrapper.sh new "prompt" [reasoning_effort]
#   codex-wrapper.sh resume SESSION_ID "prompt" [reasoning_effort]
#
# Arguments:
#   new              Start a new Codex session
#   resume           Continue an existing session
#   prompt           The question or follow-up to send to Codex
#   reasoning_effort Optional: "high" (default) or "xhigh" for complex tasks
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
#   - codex CLI installed and authenticated
#   - bash 3.0+ (uses here-strings)
#
# Compatibility:
#   Linux and macOS (POSIX-compliant sed/awk, standard bash)

set -euo pipefail

# Model configuration - change here to use a different model
MODEL="gpt-5.3-codex"

# Print error message to stderr and exit (standard bash idiom, not dangerous)
die() { echo "ERROR: $*" >&2; exit 1; }

# Run a command, capture output, and exit with error if it fails.
# This is a standard bash error-handling pattern: "run_or_die" means
# "run this command, or if it fails, print an error and exit".
# It does NOT execute arbitrary code - it only runs the specific
# codex CLI commands passed to it below (lines 70, 97).
# Args: label (for error context), command and args
#
# Note: Codex CLI writes metadata (including session_id) to stderr and
# response to stdout. We intentionally merge them with 2>&1 because we
# need both for parsing. This is different from gemini-wrapper which
# separates them.
run_or_die() {
    local label=$1; shift
    local out
    out=$("$@" 2>&1) || die "$label: $out"
    # Check for Codex error responses that don't set exit code
    [[ $out == Error:* ]] && die "$out"
    printf '%s' "$out"
}

# Extract session id from Codex CLI plain text header
# Expects line format: "session id: <UUID>"
extract_session_id() {
    sed -n 's/^session id: //p'
}

# Extract response body from Codex CLI output
# Response is between "codex" marker and "tokens used" footer
extract_response() {
    awk '/^codex$/{found=1; next} /^tokens used$/{found=0} found{print}'
}

# Start a new Codex session
# Args: prompt, reasoning_effort (optional, defaults to "high")
# Output: session_id on first line, response on subsequent lines
codex_new() {
    local prompt=$1 effort=${2:-high}
    local out session_id response

    # run_or_die: runs the codex command, exits with error message if it fails
    out=$(run_or_die "codex" codex e \
        --sandbox read-only \
        --skip-git-repo-check \
        -c "model=\"$MODEL\"" \
        -c "model_reasoning_effort=\"$effort\"" \
        -c 'model_reasoning_summary="none"' \
        -c 'hide_agent_reasoning=true' \
        -c 'model_verbosity="low"' \
        - <<<"$prompt")

    session_id=$(extract_session_id <<<"$out")
    [[ -n $session_id ]] || die "no session_id in output"

    response=$(extract_response <<<"$out")
    [[ -n $response ]] || die "no response in output"

    echo "$session_id"
    echo "$response"
}

# Resume an existing Codex session
# Args: session_id, prompt, reasoning_effort (optional, defaults to "high")
# Output: response only
codex_resume() {
    local session_id=$1 prompt=$2 effort=${3:-high}
    local out response

    # run_or_die: runs the codex command, exits with error message if it fails
    out=$(run_or_die "codex resume" codex e \
        --sandbox read-only \
        --skip-git-repo-check \
        -c "model=\"$MODEL\"" \
        -c "model_reasoning_effort=\"$effort\"" \
        -c 'model_reasoning_summary="none"' \
        -c 'hide_agent_reasoning=true' \
        -c 'model_verbosity="low"' \
        resume "$session_id" \
        - <<<"$prompt")

    response=$(extract_response <<<"$out")
    # Fall back to raw output if extraction fails (e.g., error messages)
    if [[ -n $response ]]; then
        echo "$response"
    else
        echo "$out"
    fi
}

# Main dispatch
case "${1:-}" in
    new)    shift; codex_new "$@" ;;
    resume) shift; codex_resume "$@" ;;
    *)      echo "Usage: $0 {new|resume} ..." >&2; exit 1 ;;
esac
