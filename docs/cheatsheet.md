# bead cheatsheet

A compact overview of how bead works: create a workspace, declare explicit inputs, write outputs, and save an immutable archive (.zip) into a box. Works with any language and file types.

## Folder roles

- `input/` — Dependencies from upstream beads (read-only, managed by bead).
- `output/` — Results to share with downstream beads; only save final deliverables here.
- `temp/` — Scratch and intermediates; cleared when saving.
- `.bead-meta/` — Internal metadata; do not edit.
- Everything else — Your code, notebooks, scripts, docs.

## Most common workflows

### 1) Start a new workspace
```bash
$ bead new my-analysis
$ cd my-analysis
```
- Put code in your own folders.
- Write final results to `output/`.

### 2) Use another bead as an input
```bash
$ bead input add raw-survey-data   # declare dependency and load it into input/
$ ls input/raw-survey-data/        # inspect files
```
- Use relative paths from `input/<name>/` in your scripts.
- To free space later:
```bash
$ bead input unload raw-survey-data
```

### 3) Update when upstream changes
```bash
$ bead input update  # pulls the latest versions of all declared inputs
```

### 4) Save an immutable archive (.zip) to a box
```bash
$ bead box add my-beads ~/bead-storage  # run once per box
$ bead save my-beads
```
- Produces a timestamped .zip archive in the box.
- Anyone can open the .zip even without bead installed.

### 5) Reopen or review a saved bead
```bash
$ bead edit <ref>            # recreate workspace for editing/re-running
$ bead edit --review <ref>   # mount outputs for review; avoid accidental edits
```
- `<ref>` can be a short bead name or a full path.

### 6) Discard a workspace (removes all files)
```bash
$ bead discard
```

## What goes where

- Final deliverables: write to `output/` (CSV, parquet, figures, README).
- Large intermediates: keep in `temp/`.
- Never write to `input/` (managed by bead).
- Include a short `output/README.md` describing files and steps.

## Language-agnostic usage

- Run any tool (bash, Python, R, Stata, Julia, SQL) as usual.
- Use relative paths; avoid hardcoded absolute paths.
- Capture environment info (e.g., `requirements.txt`, `Project.toml`) alongside outputs.

## Key commands (the essentials)

```bash
# Workspaces
$ bead new <name>              # create new workspace
$ bead edit <ref>              # recreate workspace from saved bead
$ bead edit --review <ref>     # open outputs for review
$ bead save <box>              # save immutable .zip archive to box
$ bead discard                 # delete current workspace

# Inputs (dependencies)
$ bead input add <name>        # declare and load dependency
$ bead input load <name>       # load already-declared dependency
$ bead input update            # update all declared inputs
$ bead input unload <name>     # free disk space for a dependency

# Boxes (storage)
$ bead box add <name> <path>   # register a storage location
$ bead box list                # list registered boxes
$ bead box forget <name>       # remove box reference

# Utility
$ bead version                 # print versions
```

## Quick patterns to copy

- Chain of provenance (A → B → C):
```bash
$ bead new raw-data
$ cd raw-data
# write data to output/...
$ bead save my-beads

$ bead new clean-data
$ cd clean-data
$ bead input add raw-data
# read from input/raw-data/, write to output/...
$ bead save my-beads

$ bead new final-analysis
$ cd final-analysis
$ bead input add clean-data
# read from input/clean-data/, write to output/...
$ bead save my-beads
```

- Review past results without editing:
```bash
$ bead edit --review final-analysis
```

- Free space after inspection:
```bash
$ bead input unload raw-data
```

bead gives you immutable snapshots, explicit inputs, and a clear chain of provenance—so results are reproducible and sharable beyond tomorrow.
