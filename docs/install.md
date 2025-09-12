---
layout: page
title: Installation
description: How to install bead for reproducible data analysis
permalink: /install/
---

# Installing bead

bead is a tool for managing external data dependencies in reproducible research projects. Follow these instructions to install bead on your system.

## Prerequisites

- Python 3.10 or higher
- pipx (recommended) or pip
- Git (for installation from GitHub)

## Recommended: Installation via pipx

The recommended way to install bead is using pipx, which installs Python applications in isolated environments:

```bash
# Install pipx if you don't have it
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install bead
pipx install git+https://github.com/bead-project/bead
```

This ensures bead is available globally without interfering with other Python packages.

## Alternative: Installation via pip

If you prefer using pip directly:

```bash
pip install --user git+https://github.com/bead-project/bead
```

## To force reinstall/update to the latest version

```bash
pipx install --force git+https://github.com/bead-project/bead
```

Note: Using `--user` is recommended to avoid conflicts with system packages.

## Installation from source (for development)

To install the latest development version for contributing:

```bash
git clone https://github.com/bead-project/bead
cd bead
pip install -e .
```

## Verify installation

After installation, verify that bead is working correctly:

```bash
bead version
```

This should display the installed version of bead.

## Getting started

Once installed, you can initialize a new bead project in any directory:

```bash
bead new <project-name>
```



## Next steps

- Read the [Getting Started guide]({{ '/getting-started' | relative_url }})
- Learn about [core concepts]({{ '/guides/concepts' | relative_url }})
- Explore [examples]({{ '/guides/examples' | relative_url }})

## Troubleshooting

If you encounter any issues during installation:

1. Ensure Python and pip are up to date
2. Try installing in a virtual environment
3. Check the [GitHub issues](https://github.com/bead-project/bead/issues) for known problems
4. Report new issues with detailed error messages

## System requirements

bead works on:
- Linux
- macOS
- Windows (with Python installed)

### SQLite Index (v0.9+)

Starting with version 0.9, bead uses SQLite to index bead boxes for improved performance. The SQLite database (`.index.sqlite`) is automatically created in each box directory when you:

- Add a new box with `bead box add`
- Save beads to a box with `bead save`
- Rebuild the index with `bead box rebuild`
- Sync the index with `bead box sync`

This index enables fast searching and dependency resolution across large collections of beads. No additional SQLite installation is required as Python includes SQLite support by default.

bead has minimal system requirements and should work on any system where Python runs.