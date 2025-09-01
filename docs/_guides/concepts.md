---
title: Core Concepts
description: Understanding bead's fundamental principles and design
order: 1
---

## The bead Philosophy

Research workflows are complex and hard to reproduce. Data files get moved, code gets updated, team members leave, and suddenly results can't be recreated. bead solves this with a simple approach: **package everything needed to recreate a result into one self-contained unit**.

This creates reproducible computational workflows without forcing you to change how you work.

### The Fundamental Pattern

```
output = code(*inputs)
```

Every bead follows this pattern:
- **Inputs**: The data you need (bead tracks exactly which version)
- **Code**: Your scripts, notebooks, whatever (bead saves all of it)  
- **Output**: The results you created (bead packages it up nicely)

## Key Concepts

### 1. Immutable Computational Snapshots

When you save a bead, it becomes an immutable archive containing:
- All code needed to run the computation
- References to exact input data versions  
- Generated output files
- Metadata about creation time and dependencies

Think of it as a computational snapshot. You can always return to recreate the exact same results.

## Who This Is Actually For

**You'll love bead if you:**
- Work with data and write code to analyze it
- Have ever asked "what data did I use for this?" 
- Need to share analysis with teammates
- Want to actually reproduce your own work months later
- Use Python, R, Stata, Julia, shell scripts, or really anything
- Care more about getting stuff done than learning new frameworks

**You might want something else if you:**
- Just need to track code changes (use Git)
- Want a workflow orchestrator (try Airflow or similar)  
- Need to manage software installations (use conda/Docker)
- Are building web apps or mobile apps (this is for data analysis)

### 2. Workspace vs Archive

**Workspace** (Active Development)
- Directory where you actively work on analysis
- You can modify files, run code, test ideas
- Temporary state during development

**Archive** (Saved bead)
- Immutable ZIP file stored in a bead box
- Timestamped and content-verified
- The permanent, shareable record of your computation

```bash
# Workspace: active development
$ cd my-analysis/
$ python analyze.py  # Modify and test

# Archive: frozen snapshot  
$ bead save results
# Creates: my-analysis_20250730T120000+0200.zip
```

### 3. Content-Based Verification

Every file in a bead has a cryptographic hash. When you load dependencies, bead verifies you have the exact same files that produced the original results.

```bash
$ bead input add processed-data
# bead verifies:
# - Correct version exists
# - Content matches hash
# - No corruption occurred
```

### 4. Directed Acyclic Graphs (DAGs)

beads form dependency graphs:

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

bead doesn't care about your tools:
- Use any programming language
- Use any data format
- Use any execution method

bead only manages files and dependencies.

### 4. Human-Readable Archives

Even without bead installed, archives are usable:

```bash
$ unzip analysis_20250730T120000.zip
$ ls
code/       # Your source code files
data/       # Output data from your analysis
meta/       # bead metadata (bead, input.map, manifest)
```

## The bead Lifecycle

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

## What bead Is NOT

Understanding what bead doesn't do is as important as what it does:

### Not a Version Control System
- bead tracks computational snapshots, not code evolution
- Use Git for code versioning within beads
- bead complements, doesn't replace, traditional VCS

### Not a Workflow Engine
- bead doesn't execute your code
- No job scheduling or parallelization
- You control execution, bead manages artifacts

### Not a Data Store
- bead manages references, not data hosting
- No cloud storage or synchronization
- You manage where bead boxes live

### Not a Package Manager
- bead doesn't install software dependencies
- Use conda, pip, or system packages
- Document environment in your bead

## Common Patterns

### Source beads
No inputs, only outputs:
```bash
$ bead new survey-data
$ curl -o output/responses.csv https://survey.com/data
$ bead save raw-data
```

### Processing beads
Transform inputs to outputs:
```bash
$ bead new clean-survey
$ bead input add survey-data
$ python clean.py input/survey-data/responses.csv output/clean.csv
$ bead save processed
```

### Analysis beads
Final computations, often never closed:
```bash
$ bead new paper-figures
$ bead input add clean-survey
$ R --file=analyze.R
# May never 'bead save' - just share outputs directly
```

## Best Practices

### 1. One Concept, One bead
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