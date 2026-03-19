#!/bin/bash
# Kimi API wrapper for kimi-ask skill
#
# Provides a simplified interface to Moonshot/Kimi API for the deliberation protocol.
# Handles session creation (with conversation history) and resumption via curl.
#
# Usage:
#   kimi-wrapper.sh new "prompt" [effort]
#   kimi-wrapper.sh resume SESSION_ID "prompt" [effort]
#
# Arguments:
#   new              Start a new Kimi session
#   resume           Continue an existing session
#   prompt           The question or follow-up to send to Kimi
#   effort           Optional: "high" (default) or "xhigh" (enables thinking mode)
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
#   - MOONSHOT_API_KEY environment variable set
#   - curl, jq
#   - bash 3.0+ (uses here-strings)
#   - uuidgen (standard on macOS/Linux)
#
# Compatibility:
#   Linux and macOS (POSIX-compliant, standard bash)

set -euo pipefail

: "${MOONSHOT_API_KEY:?export MOONSHOT_API_KEY=...}"
BASE_URL="${MOONSHOT_BASE_URL:-https://api.moonshot.ai/v1}"

# Model configuration
MODEL="kimi-k2.5"

# Conversation history directory (NDJSON: one JSON object per line)
HISTORY_DIR="$HOME/.claude/skills/kimi-ask/deliberations"

# Print error message to stderr and exit
die() { echo "ERROR: $*" >&2; exit 1; }

# Get history file path for a session
history_file() { echo "$HISTORY_DIR/${1}-history.jsonl"; }

# Build request JSON from messages array and effort level
build_request() {
    local messages_json=$1 effort=${2:-high}
    local thinking_frag=
    # kimi-k2.5 only accepts temperature=1
    [[ "$effort" == "xhigh" ]] && thinking_frag=', "thinking": {"type": "enabled"}'
    jq -n \
        --arg model "$MODEL" \
        --argjson messages "$messages_json" \
        '{model: $model, messages: $messages, temperature: 1}'"$thinking_frag"
}

# Send request to Kimi API and return response JSON
# Uses stdin pipe to bypass ARG_MAX limits on large request payloads
send_request() {
    local req_json=$1
    local resp

    resp=$(printf '%s' "$req_json" | curl -sS \
        --connect-timeout 10 \
        --max-time 1500 \
        -H "Authorization: Bearer $MOONSHOT_API_KEY" \
        -H "Content-Type: application/json" \
        --data-binary @- \
        "$BASE_URL/chat/completions" 2>&1) || die "API call failed: $resp"

    # Check for API error response
    local error_msg
    error_msg=$(jq -r '.error.message // empty' <<<"$resp" 2>/dev/null)
    [[ -n "$error_msg" ]] && die "API error: $error_msg"

    printf '%s' "$resp"
}

# Extract assistant content from API response
extract_content() {
    jq -r '.choices[0].message.content // empty'
}

# Start a new Kimi session
# Args: prompt, effort (optional, defaults to "high")
# Output: session_id on first line, response on subsequent lines
kimi_new() {
    local prompt=$1 effort=${2:-high}
    local session_id messages_json req_json resp_json content

    session_id=$(uuidgen | tr '[:upper:]' '[:lower:]')
    mkdir -p "$HISTORY_DIR"

    # Build initial messages array
    messages_json=$(jq -n --arg prompt "$prompt" '[{role: "user", content: $prompt}]')

    req_json=$(build_request "$messages_json" "$effort")
    resp_json=$(send_request "$req_json")

    content=$(extract_content <<<"$resp_json")
    [[ -n "$content" ]] || die "no content in response"

    # Save conversation history as NDJSON (one message per line, atomic write)
    local hfile
    hfile=$(history_file "$session_id")
    jq -n --arg prompt "$prompt" --arg content "$content" \
        '{role: "user", content: $prompt}, {role: "assistant", content: $content}' \
        > "$hfile"

    printf '%s\n' "$session_id"
    printf '%s\n' "$content"
}

# Resume an existing Kimi session
# Args: session_id, prompt, effort (optional, defaults to "high")
# Output: response only
kimi_resume() {
    local session_id=$1 prompt=$2 effort=${3:-high}
    local hfile messages_json req_json resp_json content

    hfile=$(history_file "$session_id")
    [[ -f "$hfile" ]] || die "no history file for session $session_id"

    # Load existing NDJSON conversation and append new user message
    messages_json=$(jq -s --arg prompt "$prompt" '. + [{role: "user", content: $prompt}]' "$hfile")

    req_json=$(build_request "$messages_json" "$effort")
    resp_json=$(send_request "$req_json")

    content=$(extract_content <<<"$resp_json")
    [[ -n "$content" ]] || die "no content in response"

    # Append new exchange to history (atomic rewrite preserves NDJSON integrity)
    jq -s --arg prompt "$prompt" --arg content "$content" \
        '.[] , {role: "user", content: $prompt} , {role: "assistant", content: $content}' \
        "$hfile" > "${hfile}.tmp" && mv "${hfile}.tmp" "$hfile"

    printf '%s\n' "$content"
}

# Main dispatch
case "${1:-}" in
    new)    shift; kimi_new "$@" ;;
    resume) shift; kimi_resume "$@" ;;
    *)      echo "Usage: $0 {new|resume} ..." >&2; exit 1 ;;
esac
