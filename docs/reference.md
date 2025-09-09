---
layout: page
title: CLI Reference
description: Complete command reference for bead
---

# bead CLI Reference

Complete reference for all bead commands and options.

## Global Options

```bash
bead [-h] [--help] <command> [<args>]

Options:
  -h, --help   Show help message

Commands:
  new          Create and initialize new workspace
  edit         Create workspace from specified bead
  discard      Delete workspace
  save         Save workspace in a box
  status       Show workspace information
  web          Manage/visualize dependency graphs
  nuke         Delete workspace (alias for discard)
  version      Show program version
  input        Manage data from other beads
  box          Manage bead boxes
```

## Version Information

### `bead version`

Show bead and Python version information.

```bash
bead version [-h]

Example:
  $ bead version
  
  Python:
  ------
  3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 15.0.0]
  
  Bead:
  ----
  0.9.0.dev1
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

### `bead edit`

Create workspace from specified bead (formerly `develop`).

```bash
bead edit <bead-ref> [<workspace>] [-t TIME] [--review]

Arguments:
  bead-ref     Bead name, timestamp, or archive path
  workspace    Directory for workspace (default: derive from bead name)

Options:
  -t, --time TIME    Use specific version timestamp (default: latest)
  --review           Include output data for review

Examples:
  $ bead edit my-analysis                    # Latest version
  $ bead edit my-analysis_20250730T120000.zip  # Specific version
  $ bead edit --review my-analysis            # With outputs
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

### `bead discard` / `bead nuke`

Delete workspace directory (handles read-only input folders).

```bash
bead discard [<workspace>] [-f|--force]
bead nuke [<workspace>] [-f|--force]  # Alias for discard

Arguments:
  workspace    Directory to delete (default: current directory)

Options:
  -f, --force  Delete even if not a valid workspace (DANGER!)

Examples:
  $ bead discard
  Deleted workspace /path/to/workspace
  
  $ bead discard ../old-project
  $ bead nuke -f damaged-workspace  # Force delete
```

## Input Management

### `bead input add`

Define dependency and load its data.

```bash
bead input add <input-name> [<bead-ref>] [-t TIME] [-w WORKSPACE]

Arguments:
  input-name   Name for this input in your workspace
  bead-ref     Source bead (default: same as input-name)

Options:
  -t, --time TIME        Use specific version timestamp
  -w, --workspace DIR    Workspace directory

Examples:
  $ bead input add survey-data
  $ bead input add responses survey-2024
  $ bead input add old-model model -t 20250601T000000+0200
```

### `bead input load`

Load data from already defined dependency.

```bash
bead input load [<input-name>] [-w WORKSPACE]

Arguments:
  input-name   Specific input to load (default: all inputs)

Options:
  -w, --workspace DIR    Workspace directory

Examples:
  $ bead input load survey-data
  $ bead input load  # Load all inputs
```

### `bead input update`

Update input[s] to newest version or defined bead.

```bash
bead input update [<input-name>] [<bead-ref>] [-t TIME] [-N] [-P] [-w WORKSPACE]

Arguments:
  input-name   Specific input to update (default: all inputs)
  bead-ref     Bead to load data from (default: same bead, newest version)

Options:
  -t, --time TIME        Use specific version timestamp
  -N, --next             Update to next version
  -P, --prev, --previous Update to previous version
  -w, --workspace DIR    Workspace directory

Examples:
  $ bead input update processed-data
  $ bead input update  # Update all inputs
  $ bead input update -P my-model  # Previous version
  $ bead input update data-input other-bead  # Remap to different bead
```

### `bead input unload`

Remove input data but keep dependency definition.

```bash
bead input unload [<input-name>] [-w WORKSPACE]

Arguments:
  input-name   Specific input to unload (default: all inputs)

Options:
  -w, --workspace DIR    Workspace directory

Examples:
  $ bead input unload large-dataset
  $ bead input unload  # Unload all inputs
```

### `bead input delete` / `bead input rm`

Remove input dependency entirely.

```bash
bead input delete <input-name> [-w WORKSPACE]
bead input rm <input-name> [-w WORKSPACE]  # Alias for delete

Arguments:
  input-name   Input to remove

Options:
  -w, --workspace DIR    Workspace directory

Examples:
  $ bead input delete old-data
  $ bead input rm unused-model
```

## Box Management

bead boxes are storage locations for your bead archives. Starting with version 0.9+, boxes use SQLite indexes for fast searching and dependency resolution. The `.index.sqlite` file in each box directory maintains metadata about all beads stored there.

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

## Workspace Information

### `bead status`

Show workspace information and input status.

```bash
bead status [-w WORKSPACE] [-v]

Options:
  -w, --workspace DIR    Workspace directory
  -v, --verbose          Show more detailed information

Example:
  $ bead status
  Workspace: my-analysis
  Created: 2025-07-30T12:00:00+02:00
  Inputs:
    ✓ processed-data (loaded)
    ✗ model-config (not loaded)
    
  $ bead status -v  # More detailed output
```

## Metadata Commands

### `bead meta`

View bead metadata.

```bash
bead meta [-w <workspace>]

Example:
  $ bead meta
  bead: my-analysis
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
│   ├── bead            # bead specification
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
$ bead discard my-analysis
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