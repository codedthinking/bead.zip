---
title: Dependency Management
description: Building complex computational graphs with Bead's input system
order: 2
---

## Understanding Dependencies

In Bead, dependencies are explicit connections between computational units. When bead B depends on bead A, it means B uses A's outputs as inputs.

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
├── src/
└── temp/
```

## Complete Input Commands

### Adding Dependencies

```bash
# Basic add (finds latest version)
bead input add survey-responses

# Add with custom name
bead input add responses survey-2024

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
# Data restored from bead box
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
```

### Advanced Operations

```bash
# Remap to different source
$ bead input map old-data new-cleaned-data

# Delete dependency entirely  
$ bead input delete test-data

# List all current inputs
$ bead input list
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
$ bead input update --prev survey-data
```

### Version Conflicts

When your input is outdated:

```bash
$ bead input update
Updating processed-data:
  Current: processed-data_20250729T100000+0200.zip
  Latest:  processed-data_20250730T150000+0200.zip
Update? [y/N]: y
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

# Use in analysis
$ cat > analyze.py << 'EOF'
import pandas as pd

customers = pd.read_csv('input/customer-data/customers.csv')
transactions = pd.read_csv('input/transaction-logs/logs.csv')
products = pd.read_csv('input/product-catalog/products.csv')

# Merge and analyze...
EOF
```

### Dependency Chains

Build pipelines where each step depends on the previous:

```bash
# Step 1: Raw data
bead new raw-sensor-readings
# ... download data ...
bead save data-lake

# Step 2: Cleaning  
bead new clean-sensor-data
bead input add raw-sensor-readings
# ... clean data ...
bead save processed

# Step 3: Analysis
bead new sensor-analysis
bead input add clean-sensor-data
# ... analyze ...
bead save results

# Step 4: Visualization
bead new dashboard
bead input add sensor-analysis
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
$ bead input add base-data

$ bead new temporal-analysis  
$ bead input add base-data

$ bead new cohort-analysis
$ bead input add base-data
```

## Managing Large Dependencies

### Selective Loading with -x Flag

For beads with large outputs:

```bash
# Development: don't load outputs
$ bead develop large-model-results

# When you need to inspect outputs
$ bead develop -x large-model-results
```

### Partial Dependencies

When you only need some files:

```bash
# In your code, check what's available
import os

if os.path.exists('input/large-data/subset.csv'):
    # Use subset for development
    data = pd.read_csv('input/large-data/subset.csv')
else:
    # Full data in production
    data = pd.read_csv('input/large-data/full.csv')
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
```

### Wrong Version Loaded

```bash
# Check current version
$ ls -la input/processed-data/
# Check timestamp in filename

# Update to latest
$ bead input update processed-data

# Or pin to specific version
$ bead input map processed-data processed-data_20250730T120000+0200.zip
```

### Circular Dependencies

Bead prevents circular dependencies:

```bash
$ bead input add analysis-b
ERROR: Circular dependency detected:
  analysis-a → analysis-b → analysis-a
```

Solution: Refactor into proper DAG:
```bash
# Extract common elements
$ bead new shared-preprocessing
# Both analyses can depend on this
```

## Best Practices

### 1. Descriptive Input Names

```bash
# Match input name to source bead
$ bead input add customer-demographics

# Clear names in code
demographics = pd.read_csv('input/customer-demographics/data.csv')
```

### 2. Document Dependencies

In your README:
```markdown
## Dependencies

This bead requires:
- `survey-responses`: Raw survey data (v2024-07-30 or later)
- `census-data`: Population statistics for weighting
```

### 3. Test with Different Versions

```bash
# Test with latest
$ bead input update
$ make test

# Test with production version
$ bead input map survey-data survey-data_20250701T000000+0200.zip
$ make test
```

### 4. Handle Missing Inputs Gracefully

```python
import os
import sys

required_inputs = ['survey-data', 'model-parameters']
for inp in required_inputs:
    if not os.path.exists(f'input/{inp}'):
        print(f"ERROR: Required input '{inp}' not loaded")
        print(f"Run: bead input load {inp}")
        sys.exit(1)
```

## Advanced Patterns

### Conditional Dependencies

```python
# config.json specifies which inputs to use
config = json.load(open('config.json'))

if config['use_external_data']:
    if not os.path.exists('input/external-source'):
        raise ValueError("External data not loaded")
    external = pd.read_csv('input/external-source/data.csv')
```

### Dependency Versioning in Analysis

Track which versions produced results:

```python
# Record input versions in output
import os
import json

versions = {}
for input_dir in os.listdir('input'):
    # Get version from symlink or metadata
    versions[input_dir] = get_input_version(input_dir)

with open('output/input-versions.json', 'w') as f:
    json.dump(versions, f, indent=2)
```

### Multi-Stage Processing

```bash
# Stage 1: Quick prototype with subset
$ bead input add data-subset
$ python prototype.py
$ bead save prototype

# Stage 2: Full analysis with complete data  
$ bead input delete data-subset
$ bead input add data-complete
$ python full_analysis.py
$ bead save final
```

Ready to collaborate? Continue to [Team Collaboration](/guides/collaboration) to learn how teams work together with Bead.