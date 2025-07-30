---
layout: page
title: CLI Reference
description: Complete command reference for Bead
---

# Bead CLI Reference

Complete reference for all Bead commands and options.

## Global Options

```bash
bead [--version] [--help] <command> [<args>]

Options:
  --version    Show version information
  --help       Show help message
  -w PATH      Workspace directory (default: current directory)
```

## Core Commands

### `bead new`

Create a new bead workspace.

```bash
bead new <name> [-w <workspace>]

Arguments:
  name         Name of the new bead

Example:
  $ bead new customer-analysis
  Created "customer-analysis"
```

### `bead develop`

Open an existing bead for development.

```bash
bead develop <bead-ref> [-w <workspace>] [-x|--extract-output]

Arguments:
  bead-ref     Bead name, timestamp, or archive path

Options:
  -x, --extract-output    Also extract output data

Examples:
  $ bead develop my-analysis                    # Latest version
  $ bead develop my-analysis_20250730T120000.zip  # Specific version
  $ bead develop -x my-analysis                 # With outputs
```

### `bead save`

Save current workspace as a new bead archive.

```bash
bead save <box> [-w <workspace>]

Arguments:
  box          Name of the bead box to save to

Example:
  $ bead save production
  Successfully stored bead at /path/to/box/my-bead_20250730T120000.zip
```

### `bead zap`

Delete a workspace (handles read-only input folders).

```bash
bead zap [-w <workspace>]

Example:
  $ bead zap
  Workspace deleted
```

## Input Management

### `bead input add`

Add a new input dependency.

```bash
bead input add <input-name> [<bead-ref>] [--time TIME]

Arguments:
  input-name   Name for this input in your workspace
  bead-ref     Source bead (default: same as input-name)

Options:
  --time TIME  Use specific version timestamp

Examples:
  $ bead input add survey-data
  $ bead input add responses survey-2024
  $ bead input add old-model model --time 20250601T000000+0200
```

### `bead input load`

Load data for existing input dependencies.

```bash
bead input load [<input-name>] [--all]

Arguments:
  input-name   Specific input to load

Options:
  --all        Load all defined inputs

Examples:
  $ bead input load survey-data
  $ bead input load --all
```

### `bead input update`

Update inputs to newer versions.

```bash
bead input update [<input-name>] [--all] [--time TIME] [--prev]

Arguments:
  input-name   Specific input to update

Options:
  --all        Update all inputs
  --time TIME  Update to specific timestamp
  --prev       Update to previous version

Examples:
  $ bead input update processed-data
  $ bead input update --all
  $ bead input update --prev my-model
```

### `bead input unload`

Remove input data but keep dependency definition.

```bash
bead input unload <input-name>

Example:
  $ bead input unload large-dataset
  Input data removed (definition kept)
```

### `bead input delete`

Remove input dependency entirely.

```bash
bead input delete <input-name>

Example:
  $ bead input delete old-data
  Input dependency removed
```

### `bead input map`

Remap input to different source bead.

```bash
bead input map <input-name> <new-bead-ref>

Example:
  $ bead input map test-data production-data
  Input remapped
```

## Box Management

### `bead box add`

Define a new bead box (storage location).

```bash
bead box add <name> <path>

Arguments:
  name         Friendly name for the box
  path         Directory path for storage

Example:
  $ bead box add shared /mnt/team/beads
  Box 'shared' added
```

### `bead box list`

List all configured bead boxes.

```bash
bead box list

Example:
  $ bead box list
  Boxes:
  -------------
  local: /home/user/beads
  shared: /mnt/team/beads
  archive: /backup/bead-archive
```

### `bead box forget`

Remove a box from configuration.

```bash
bead box forget <name>

Example:
  $ bead box forget old-storage
  Box forgotten
```

## Web Visualization

### `bead web`

Generate and manipulate dependency graph visualizations.

```bash
bead web <command> [args...]

Commands:
  load <file>              Load saved web graph
  save <file>              Save current web graph
  / <sources..> / <sinks..> /    Filter by sources/sinks
  heads                    Show only latest versions
  color                    Apply freshness coloring
  png <file>              Generate PNG visualization
  svg <file>              Generate SVG visualization
  view <file>              Open visualization in browser

Example Pipeline:
  $ bead web heads color png graph.png view graph.png
```

## Metadata Commands

### `bead meta`

View bead metadata.

```bash
bead meta [-w <workspace>]

Example:
  $ bead meta
  Bead: my-analysis
  Created: 2025-07-30T12:00:00+02:00
  Inputs: processed-data, model-config
```

### `bead xmeta`

Export extended metadata.

```bash
bead xmeta <bead-archive>

Example:
  $ bead xmeta my-analysis_20250730.zip > metadata.json
```

## Environment Variables

### `BEAD_PATH`

Colon-separated list of directories to search for bead boxes.

```bash
export BEAD_PATH=/shared/beads:/archive/beads
```

### `BEAD_WORKSPACE`

Default workspace directory.

```bash
export BEAD_WORKSPACE=/home/user/current-bead
```

## File Structure

### Workspace Layout

```
workspace/
├── .bead-meta/          # Metadata (don't edit)
│   ├── bead            # Bead specification
│   └── input.map       # Input mappings
├── input/              # Input dependencies (read-only)
│   └── <input-name>/   # One folder per input
├── output/             # Files to share
├── temp/               # Temporary files (not saved)
└── <other>/            # Your code and files
```

### Archive Structure

```
bead-name_TIMESTAMP.zip
├── code/               # All non-special directories
├── data/               # Contents of output/
└── meta/               # Metadata files
    ├── bead           # Specification
    └── manifest       # File checksums
```

## Exit Codes

- `0` - Success
- `1` - General error
- `2` - Usage error (invalid arguments)
- `3` - Workspace error (not a valid bead)
- `4` - Dependency error (missing/invalid input)
- `5` - Box error (storage issues)

## Common Workflows

### Basic Development Cycle

```bash
# 1. Create new bead
$ bead new my-analysis
$ cd my-analysis

# 2. Add dependencies
$ bead input add clean-data

# 3. Develop
$ python analyze.py

# 4. Save snapshot
$ bead save results

# 5. Clean up
$ cd ..
$ bead zap my-analysis
```

### Updating Dependencies

```bash
# Check for updates
$ bead input update --dry-run

# Update all inputs
$ bead input update --all

# Rerun analysis
$ make all

# Save new version
$ bead save results
```

### Debugging Dependencies

```bash
# List current inputs
$ ls -la input/

# Check input metadata
$ cat .bead-meta/input.map

# Verify input contents
$ head input/my-data/data.csv

# Check available versions
$ ls /path/to/box/my-data_*.zip
```

For more detailed examples and patterns, see our [Guides](/guides).