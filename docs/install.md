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
- pip (Python package installer)

## Installation via pip

The easiest way to install bead is using pip:

```bash
pip install bead
```

## Installation from source

To install the latest development version from GitHub:

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