---
layout: page
title: Getting Started
description: Get up and running with reproducible research in 5 minutes
---

# Getting Started with bead

Stop asking "what data did we use?" five times a day. This guide will get you up and running with reproducible research in just a few minutes.

## Installation

### Quick Install (Recommended)

The easiest way to install bead is using pipx:

```bash
# Install pipx if you don't have it
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install bead
pipx install git+https://github.com/e3krisztian/bead.git
```

### Alternative Methods

If you prefer pip:

```bash
pip install --user git+https://github.com/e3krisztian/bead.git
```

To install the latest development version, use the `--force` flag with pipx to update:

```bash
pipx install --force git+https://github.com/e3krisztian/bead.git
```

For more installation options, see the [full installation guide]({{ '/install' | relative_url }}).

### Verify Installation

```bash
$ bead version

Python:
------
3.13.0 (main, Oct  7 2024, 05:02:14) [Clang 15.0.0 (clang-1500.1.0.2.5)]

Bead:
----
0.9.0.dev1
```

## Your First bead

Let's create a simple data analysis workflow to understand how bead works.

### 1. Create a New bead

```bash
$ bead new my-first-analysis
Created "my-first-analysis"

$ cd my-first-analysis
$ ls -la
drwxr-xr-x  .bead-meta/
drwxr-xr-x  input/
drwxr-xr-x  output/
drwxr-xr-x  temp/
```

### 2. Understanding the Directory Structure

bead creates these folders, each with a specific purpose:

- **`input/`** - Dependencies from other beads (read-only, managed by bead)
- **`output/`** - Files you want to share with downstream beads
- **`temp/`** - Temporary files (deleted when you save the bead)
- **`.bead-meta/`** - Internal metadata (don't modify directly)
- **Everything else** - Your code, documentation, and other files

### 3. Add Some Code

Create a simple analysis script in `src/analyze.py`:

```python
#!/usr/bin/env python3
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Save results
data.to_csv('output/results.csv', index=False)
print("Analysis complete! Results saved to output/results.csv")
```

```bash
$ mkdir src
$ # Create src/analyze.py with the code above
```

### 4. Run Your Analysis

```bash
$ python src/analyze.py
Analysis complete! Results saved to output/results.csv

$ ls output/
results.csv
```

### 5. Save Your bead

Create an immutable snapshot of your work:

```bash
# First, create a bead box (storage location)
$ bead box add my-beads ~/bead-storage
$ bead box list
Boxes:
-------------
my-beads: /Users/you/bead-storage

# Save your bead to the 'my-beads' box
$ bead save my-beads
Successfully stored bead at /Users/you/bead-storage/my-first-analysis_20250730T120000000000+0200.zip
```

## Working with Dependencies

The real power of bead comes from linking computations together.

### 1. Create a Data Source bead

```bash
$ cd ..
$ bead new raw-data
$ cd raw-data

# Download some data
$ curl -o output/data.csv https://example.com/sample-data.csv

# Save it
$ bead save my-beads
$ cd ..
```

### 2. Use Data in Another bead

```bash
$ bead new data-processing
$ cd data-processing

# Add the raw data as a dependency
$ bead input add raw-data

# Check what was loaded
$ ls input/raw-data/
data.csv

# Create processing script
# process.py:
```python
import pandas as pd

# Load input data
df = pd.read_csv('input/raw-data/data.csv')

# Process it
df_cleaned = df.dropna()
df_cleaned['processed'] = True

# Save output
df_cleaned.to_csv('output/processed_data.csv', index=False)
```

```bash
$ python process.py
$ bead save my-beads
```

## Best Practices

### 1. Clear Folder Usage

```bash
# ✅ Good: Created data in output/
df_cleaned.to_csv('output/processed_data.csv', index=False)

# ❌ Bad: Created data in temp/ (will be lost!)
df_cleaned.to_csv('temp/dataset.csv', index=False)

# ✅ Good: Intermediate files in temp/
python preprocess.py > temp/intermediate.pkl
python analyze.py temp/intermediate.pkl > output/final.csv
```

### 2. Documentation

It is good practice to include a README in your output folder. This will be loaded together with the data and your collaborators will thank you! Example `output/README.md`:

```markdown
# Processed Customer Data

This dataset contains cleaned customer records from the 2024 survey.

## Files
- `processed_data.csv`: Clean customer data with outliers removed

## Processing Steps
1. Removed rows with missing customer IDs
2. Standardized date formats
3. Removed statistical outliers (>3 std dev)

Generated: 2025-07-30
```

### 3. Reproducible Environments

Include your software dependencies:

```bash
# For Python projects
$ pip freeze > requirements.txt

# For R projects  
$ R -e "sessionInfo()" > session-info.txt

# For conda environments
$ conda env export > environment.yml
```

## Common Commands Reference

```bash
# Create and manage workspaces
bead new <name>              # Create new bead
bead edit <bead-ref>         # Open existing bead
bead edit --review <ref>     # Open with output data to review
bead save <box>              # Save to bead box
bead discard                 # Delete workspace

# Manage dependencies
bead input add <name>        # Add and load dependency
bead input load <name>       # Load existing dependency
bead input update            # Update all dependencies
bead input unload <name>     # Unload dependency and free disk space

# Manage storage
bead box add <name> <path>   # Add storage location
bead box list                # List all boxes
bead box forget <name>       # Remove box reference
```

## What's Next?

- Read the [Core Concepts]({{ '/guides/concepts' | relative_url }}) guide to understand bead's philosophy
- Learn about [Dependency Management]({{ '/guides/dependencies' | relative_url }}) for complex workflows
- Explore [Team Collaboration]({{ '/guides/collaboration' | relative_url }}) patterns

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/e3krisztian/bead/issues)
- **Documentation**: [Full Reference](/reference)

Ready to make your research reproducible? Start creating beads!