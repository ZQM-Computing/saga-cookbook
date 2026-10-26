# Inspect the installed SAGA command-line interface

This first pattern checks that `saga_cmd` is available and captures its help/usage output for troubleshooting. It does not assume that a particular library or module identifier exists across installations.

## Prerequisites

- SAGA GIS 9.12.4 (or a compatible installation) with `saga_cmd` on `PATH`
- Bash

## Run

```bash
bash examples/01-cmd-basics/inspect-cli.sh build/saga-cli-help.txt
```

The script writes the CLI's help output to the requested file and fails if the executable is missing or produces no output. It does not certify that raster-processing modules are installed or run a terrain algorithm; those are follow-up runtime patterns.

## Validation boundary

CI checks script syntax and contract assertions. To verify the installed runtime, execute the script on a host with SAGA installed and inspect the captured version/usage information.
