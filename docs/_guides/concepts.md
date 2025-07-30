---
title: Core Concepts
description: Understanding Bead's fundamental principles and architecture
order: 1
---

## The Bead Philosophy

Bead implements a simple but powerful idea: every computation should be packaged as a self-contained, immutable unit that explicitly declares its dependencies.

### The Fundamental Equation

```
output = code(*inputs)
```

This equation drives everything in Bead:
- **Output**: The results of your computation
- **Code**: Your scripts, programs, and logic  
- **Inputs**: Data from other beads (explicit dependencies)

## Key Concepts

### 1. Beads as Frozen Computations

A bead is an immutable archive containing:
- All code needed to run the computation
- References to exact input data versions
- Generated output files
- Metadata about creation time and dependencies

Think of it as a "computational photograph" - a snapshot of everything needed to reproduce a specific result.

### 2. Workspace vs Archive

**Workspace** (Open Bead)
- Active directory where you work
- Can modify files, run code, test ideas
- Temporary state during development

**Archive** (Closed Bead)
- Immutable ZIP file in a bead box
- Timestamped and content-verified
- The permanent record of your computation

```bash
# Workspace: active development
$ cd my-analysis/
$ python analyze.py  # Modify and test

# Archive: frozen snapshot  
$ bead save results
# Creates: my-analysis_20250730T120000+0200.zip
```

### 3. Content-Based Verification

Every file in a bead has a cryptographic hash. When you load dependencies, Bead verifies you have the exact same files that produced the original results.

```bash
$ bead input add processed-data
# Bead verifies:
# - Correct version exists
# - Content matches hash
# - No corruption occurred
```

### 4. Directed Acyclic Graphs (DAGs)

Beads form dependency graphs:

```
raw-data
    ↓
cleaning-step
    ↓
analysis → paper
    ↓
figures
```

Rules:
- Dependencies flow in one direction
- No circular dependencies allowed
- Each node is independently reproducible

## Design Principles

### 1. Immutability

Once saved, beads never change. New work creates new versions:

```bash
$ bead save results  # Creates v1: analysis_20250730T120000.zip
# Make changes...
$ bead save results  # Creates v2: analysis_20250730T130000.zip
# Both versions preserved forever
```

### 2. Explicit Dependencies

No hidden data sources or magic file paths:

```python
# ❌ Bad: Hidden dependency
data = pd.read_csv("/shared/data/important.csv")

# ✅ Good: Explicit bead input
data = pd.read_csv("input/validated-data/important.csv")
```

### 3. Tool Agnosticism

Bead doesn't care about your tools:
- Use any programming language
- Use any data format
- Use any execution method

Bead only manages files and dependencies.

### 4. Human-Readable Archives

Even without Bead installed, archives are usable:

```bash
$ unzip analysis_20250730T120000.zip
$ ls
code/       # All your scripts
data/       # Output data  
meta/       # Metadata files
```

## The Bead Lifecycle

### 1. Creation
```bash
$ bead new my-analysis
# Empty workspace with standard structure
```

### 2. Development
```bash
$ cd my-analysis
# Add code, load inputs, generate outputs
$ bead input add upstream-data
$ python process.py
```

### 3. Preservation
```bash
$ bead save results
# Immutable snapshot created
```

### 4. Sharing
```bash
# Copy ZIP file to collaborator
# They can reproduce exactly
$ bead develop my-analysis_20250730T120000.zip
```

### 5. Building Upon
```bash
$ bead new follow-up
$ bead input add my-analysis
# Previous outputs become new inputs
```

## What Bead Is NOT

Understanding what Bead doesn't do is as important as what it does:

### Not a Version Control System
- Bead tracks computational snapshots, not code evolution
- Use Git for code versioning within beads
- Bead complements, doesn't replace, traditional VCS

### Not a Workflow Engine
- Bead doesn't execute your code
- No job scheduling or parallelization
- You control execution, Bead manages artifacts

### Not a Data Store
- Bead manages references, not data hosting
- No cloud storage or synchronization
- You manage where bead boxes live

### Not a Package Manager
- Bead doesn't install software dependencies
- Use conda, pip, or system packages
- Document environment in your bead

## Common Patterns

### Source Beads
No inputs, only outputs:
```bash
$ bead new survey-data
$ curl -o output/responses.csv https://survey.com/data
$ bead save raw-data
```

### Processing Beads
Transform inputs to outputs:
```bash
$ bead new clean-survey
$ bead input add survey-data
$ python clean.py input/survey-data/responses.csv output/clean.csv
$ bead save processed
```

### Analysis Beads
Final computations, often never closed:
```bash
$ bead new paper-figures
$ bead input add clean-survey
$ R --file=analyze.R
# May never 'bead save' - just share outputs directly
```

## Best Practices

### 1. One Concept, One Bead
- Don't pack unrelated computations together
- Split complex pipelines into logical steps
- Each bead should have a clear purpose

### 2. Document Everything
- README in every output folder
- Explain what the bead does
- List any manual steps required

### 3. Save Frequently
- After completing meaningful work
- Before making major changes  
- When sharing with others

### 4. Use Descriptive Names
```bash
# ❌ Bad
bead new analysis
bead new data

# ✅ Good  
bead new customer-churn-model
bead new survey-2024-responses
```

Ready to dive deeper? Continue to [Dependency Management]({{ '/guides/dependencies' | relative_url }}) to learn about building complex computational graphs.