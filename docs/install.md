---
layout: page
title: Installation
description: How to install bead for reproducible data analysis
permalink: /install/
---

# Installing bead

bead is a tool for managing external data dependencies in reproducible research projects. Follow these instructions to install bead on your system.

## Prerequisites

- Python 3.7 or higher
- pipx (recommended) or pip

## Recommended: Installation via pipx

The recommended way to install bead is using pipx, which installs Python applications in isolated environments:

```bash
# Install pipx if you don't have it
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install bead
pipx install https://github.com/e3krisztian/bead
```

This ensures bead is available globally without interfering with other Python packages.

## Alternative: Installation via pip

If you prefer using pip directly:

```bash
pip install --user https://github.com/e3krisztian/bead
```

Note: Using `--user` is recommended to avoid conflicts with system packages.

## Installation from source (for development)

To install the latest development version for contributing:

```bash
git clone https://github.com/e3krisztian/bead.git
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

Or convert an existing project to use bead:

```bash
cd your-project-directory
bead init
```

## Next steps

- Read the [Getting Started guide]({{ '/getting-started' | relative_url }})
- Learn about [core concepts]({{ '/guides/concepts' | relative_url }})
- Explore [examples]({{ '/guides/examples' | relative_url }})

## Troubleshooting

If you encounter any issues during installation:

1. Ensure Python and pip are up to date
2. Try installing in a virtual environment
3. Check the [GitHub issues](https://github.com/e3krisztian/bead/issues) for known problems
4. Report new issues with detailed error messages

## System requirements

bead works on:
- Linux
- macOS
- Windows (with Python installed)

bead has minimal system requirements and should work on any system where Python runs.