#!/usr/bin/env bash
set -euo pipefail

output_path="${1:-build/saga-cli-help.txt}"
if ! command -v saga_cmd >/dev/null 2>&1; then
  echo "ERROR: saga_cmd was not found on PATH" >&2
  exit 127
fi

mkdir -p "$(dirname "$output_path")"
# Some SAGA builds return a non-zero status for help; output is checked below.
if ! saga_cmd -h >"$output_path" 2>&1; then
  :
fi
if [[ ! -s "$output_path" ]]; then
  echo "ERROR: saga_cmd produced no help output" >&2
  exit 1
fi
if ! grep -qi 'saga' "$output_path"; then
  echo "ERROR: captured output does not identify SAGA CLI" >&2
  exit 1
fi
printf 'Captured SAGA CLI help to %s\n' "$output_path"
