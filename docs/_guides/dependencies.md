---
title: Dependency Management
description: Building complex computational graphs with bead's input system
order: 2
---

## Understanding Dependencies

In bead, dependencies are explicit connections between computational units. When bead B depends on bead A, it means B uses A's outputs as inputs.

## The Input System

### Basic Dependency Addition

```bash
# Add a dependency
$ bead input add processed-data

# What happens:
# 1. Searches all bead boxes for 'processed-data'
# 2. Finds latest version
# 3. Extracts outputs to input/processed-data/
# 4. Records dependency in .bead-meta/
```

### Input Directory Structure

```
my-analysis/
├── input/
│   ├── processed-data/      # From one bead
│   │   ├── clean.csv
│   │   └── README.md
│   └── model-parameters/    # From another bead
│       └── config.json
├── output/
└── temp/
```

## Complete Input Commands

### Adding Dependencies

```bash
# Basic add (finds latest version)
bead input add survey-responses

# Add specific version
bead input add survey-responses --time 20250730T120000+0200

# Add from specific file
bead input add model-output /path/to/model_20250730.zip
```

### Loading and Unloading

Save disk space by loading/unloading large inputs:

```bash
# Unload to free space (keeps dependency definition)
$ bead input unload large-dataset
$ ls input/
# large-dataset folder gone

# Load when needed again
$ bead input load large-dataset
# Data restored from bead box at the exact same version
```

### Updating Dependencies

Keep inputs current as upstream beads evolve:

```bash
# Update single input to latest
$ bead input update processed-data

# Update all inputs
$ bead input update

# See what would update without changing
$ bead input update --dry-run

# Go back a version (helpful if you broke something)
$ bead input update --previous processed-data

# Delete dependency entirely  
$ bead input delete test-data
```

## Version Management

### Understanding Versions

Each bead save creates a new version with timestamp:
```
survey-data_20250729T100000+0200.zip  # Version 1
survey-data_20250730T100000+0200.zip  # Version 2  
survey-data_20250730T150000+0200.zip  # Version 3
```

### Pinning Versions

```bash
# Always use latest (default)
$ bead input add survey-data

# Pin to specific time
$ bead input add survey-data --time 20250730T100000+0200

# Update to previous version
$ bead input update --previous survey-data
```


## Complex Dependency Patterns

### Multiple Dependencies

```bash
$ bead new multi-source-analysis
$ cd multi-source-analysis

# Add multiple data sources
$ bead input add customer-data
$ bead input add transaction-logs  
$ bead input add product-catalog
```

Use in your analysis script (`analyze.py`):

```python
import pandas as pd

customers = pd.read_csv('input/customer-data/customers.csv')
transactions = pd.read_csv('input/transaction-logs/logs.csv')
products = pd.read_csv('input/product-catalog/products.csv')

# Merge and analyze...
```

### Dependency Chains

Build pipelines where each step depends on the previous:

```bash
# Step 1: Raw data
$ bead new raw-sensor-readings
$ cd raw-sensor-readings
# ... download data ...
bead save my-beads

# Step 2: Cleaning
$ bead new clean-sensor-data
$ cd clean-sensor-data
$ bead input add raw-sensor-readings
# ... clean data ...
$ bead save my-beads

# Step 3: Analysis
$ bead new sensor-analysis
$ cd sensor-analysis
$ bead input add clean-sensor-data
# ... analyze ...
$ bead save my-beads

# Step 4: Visualization
$ bead new dashboard
$ cd dashboard
$ bead input add sensor-analysis
# ... create plots ...
```

### Branching Dependencies

One bead can be input to many:

```
        ┌→ regional-analysis
        │
base-data──→ temporal-analysis
        │
        └→ cohort-analysis
```

Implementation:
```bash
# Each analysis starts with same base
$ bead new regional-analysis
$ cd regional-analysis
$ bead input add base-data

$ bead new temporal-analysis
$ cd temporal-analysis
$ bead input add base-data

$ bead new cohort-analysis
$ cd cohort-analysis
$ bead input add base-data
```

## Managing Large Dependencies

### Selective Loading with --review Flag

For beads with large outputs:

```bash
# Development: don't load outputs
$ bead edit large-model-results

# When you need to inspect outputs
$ bead edit --review large-model-results
```

## Troubleshooting Dependencies

### Missing Dependencies

```bash
$ python analyze.py
FileNotFoundError: input/model-output/predictions.csv

# Solution 1: Load the input
$ bead input load model-output

# Solution 2: Check if input is defined
$ cat .bead-meta/bead | grep model-output

# if not defined, add it
$ bead input add model-output
```

### Wrong Version Loaded

```bash
# Check current version
$ bead status
Bead Name: clean-sensor-data

Inputs:

input/raw-sensor-readings
	Status:      loaded
	Bead:        raw-sensor-readings # 20250909T120353663121+0100
	Box[es]:
	 * -r my-beads # 20250909T120353663121+0100

# Update to latest
$ bead input update raw-sensor-readings
```


Ready to collaborate? Continue to [Team Collaboration]({{ '/guides/collaboration' | relative_url }}) to learn how teams work together with bead.