---
layout: page
title: Getting Started
description: Get up and running with reproducible research in 5 minutes
---

# Getting Started with Bead

Stop asking "what data did we use?" five times a day. This guide will get you up and running with reproducible research in just a few minutes.

## Installation

### macOS / Linux

```bash
# Download and install bead
curl -sSL https://bead.zip/install.sh | bash

# Or with pip
pip install bead-cli
```

### Windows

```powershell
# Download the installer
Invoke-WebRequest -Uri https://bead.zip/install.ps1 -OutFile install.ps1
.\install.ps1

# Or with pip
pip install bead-cli
```

### Verify Installation

```bash
$ bead --version
bead version 1.0.0
```

## Your First Bead

Let's create a simple data analysis workflow to understand how Bead works.

### 1. Create a New Bead

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

Bead creates these folders, each with a specific purpose:

- **`input/`** - Dependencies from other beads (read-only, managed by Bead)
- **`output/`** - Files you want to share with downstream beads
- **`temp/`** - Temporary files (deleted when you save the bead)
- **`.bead-meta/`** - Internal metadata (don't modify directly)
- **Everything else** - Your code, documentation, and other files

### 3. Add Some Code

Create a simple analysis script:

```bash
$ mkdir src
$ cat > src/analyze.py << 'EOF'
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
EOF

$ chmod +x src/analyze.py
```

### 4. Run Your Analysis

```bash
$ python src/analyze.py
Analysis complete! Results saved to output/results.csv

$ ls output/
results.csv
```

### 5. Save Your Bead

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

The real power of Bead comes from linking computations together.

### 1. Create a Data Source Bead

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

### 2. Use Data in Another Bead

```bash
$ bead new data-processing
$ cd data-processing

# Add the raw data as a dependency
$ bead input add raw-data

# Check what was loaded
$ ls input/raw-data/
data.csv

# Create processing script
$ cat > process.py << 'EOF'
import pandas as pd

# Load input data
df = pd.read_csv('input/raw-data/data.csv')

# Process it
df_cleaned = df.dropna()
df_cleaned['processed'] = True

# Save output
df_cleaned.to_csv('output/processed_data.csv', index=False)
EOF

$ python process.py
$ bead save my-beads
```

## Best Practices

### 1. Clear Folder Usage

```bash
# ✅ Good: Source data in output/
echo "data" > output/dataset.csv

# ❌ Bad: Source data in temp/ (will be lost!)
echo "data" > temp/dataset.csv

# ✅ Good: Intermediate files in temp/
python preprocess.py > temp/intermediate.pkl
python analyze.py temp/intermediate.pkl > output/final.csv
```

### 2. Documentation

Always include a README in your output folder:

```bash
$ cat > output/README.md << 'EOF'
# Processed Customer Data

This dataset contains cleaned customer records from the 2024 survey.

## Files
- `processed_data.csv`: Clean customer data with outliers removed

## Processing Steps
1. Removed rows with missing customer IDs
2. Standardized date formats
3. Removed statistical outliers (>3 std dev)

Generated: 2025-07-30
EOF
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
bead develop <bead-ref>      # Open existing bead
bead develop -x <bead-ref>   # Open with output data
bead save <box>              # Save to bead box
bead zap                     # Delete workspace

# Manage dependencies
bead input add <name>        # Add and load dependency
bead input load <name>       # Load existing dependency
bead input update            # Update all dependencies
bead input unload <name>     # Free disk space

# Manage storage
bead box add <name> <path>   # Add storage location
bead box list                # List all boxes
bead box forget <name>       # Remove box reference
```

## What's Next?

- Read the [Core Concepts]({{ '/guides/concepts' | relative_url }}) guide to understand Bead's philosophy
- Learn about [Dependency Management]({{ '/guides/dependencies' | relative_url }}) for complex workflows
- Explore [Team Collaboration]({{ '/guides/collaboration' | relative_url }}) patterns
- See [Real-World Examples]({{ '/guides/examples' | relative_url }}) from research teams

## Getting Help

- **Issues**: [GitHub Issues](https://github.com/codedthinking/bead.zip/issues)
- **Discussions**: [GitHub Discussions](https://github.com/codedthinking/bead.zip/discussions)
- **Documentation**: [Full Reference](/reference)

Ready to make your research reproducible? Start creating beads!