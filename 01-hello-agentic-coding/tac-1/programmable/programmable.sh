PROMPT_CONTENT="$(cat programmable/prompt.md)"

OUTPUT="$(claude -p "$PROMPT_CONTENT")"

echo "$OUTPUT"