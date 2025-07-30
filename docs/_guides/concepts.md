---
title: Core Concepts
description: Understanding Bead's fundamental principles and design
order: 1
---

## The Bead Philosophy

Research workflows are complex and hard to reproduce. Data files get moved, code gets updated, team members leave, and suddenly results can't be recreated. Bead solves this with a simple approach: **package everything needed to recreate a result into one self-contained unit**.

This creates reproducible computational workflows without forcing you to change how you work.

### The Fundamental Pattern

```
output = code(*inputs)
```

Every bead follows this pattern:
- **Inputs**: The data you need (Bead tracks exactly which version)
- **Code**: Your scripts, notebooks, whatever (Bead saves all of it)  
- **Output**: The results you created (Bead packages it up nicely)

## Key Concepts

### 1. Immutable Computational Snapshots

When you save a bead, it becomes an immutable archive containing:
- All code needed to run the computation
- References to exact input data versions  
- Generated output files
- Metadata about creation time and dependencies

Think of it as a computational snapshot. You can always return to recreate the exact same results.

## Who This Is Actually For

**You'll love Bead if you:**
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

**Archive** (Saved Bead)
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

## How Bead Compares to Other Tools

Researchers already use many tools. Here's how Bead fits in and what makes it different:

### Bead vs Git (Version Control)

**Git tracks code changes. Bead tracks computational results.**

| **Git** | **Bead** |
|---------|----------|
| Tracks files line-by-line | Tracks computational snapshots |
| Shows what changed in code | Shows what data created results |
| Manages code evolution | Manages analysis reproducibility |
| Works on individual files | Works on complete computations |
| Merge conflicts | No conflicts (immutable archives) |

**Use together**: Git for code development, Bead for research reproducibility.

```bash
# Typical workflow using both
git add analysis.py          # Track code changes
git commit -m "Fix regression bug"
bead save results           # Capture computational snapshot
```

### Bead vs Docker (Environment Management)

**Docker packages software environments. Bead packages data workflows.**

| **Docker** | **Bead** |
|------------|----------|
| Solves "works on my machine" for software | Solves "what data did we use?" |
| Packages operating system + dependencies | Packages data + code + results |
| Runtime environment isolation | Data lineage and provenance |
| Complex setup for simple analyses | Simple setup for complex workflows |
| Great for deployment | Great for research reproduction |

**Use together**: Docker for environment consistency, Bead for data tracking.

### Bead vs Pip/Conda (Dependency Management)

**Pip/Conda manage software packages. Bead manages data dependencies.**

| **Pip/Conda** | **Bead** |
|---------------|----------|
| `pip install pandas==1.5.0` | `bead input add survey-data` |
| Software library versions | Data file versions |
| Install from package repos | Load from bead boxes |
| Environment management | Workflow management |
| Dependency conflicts possible | Content-hash verified |

**Use together**: Conda for Python packages, Bead for data inputs.

```bash
# Complete setup
conda install pandas numpy    # Software dependencies
bead input add clean-data     # Data dependencies
python analysis.py            # Run with both
```

### Bead vs Make/Snakemake (Build Systems)

**Make runs workflows. Bead preserves workflows.**

| **Make/Snakemake** | **Bead** |
|-------------------|----------|
| Executes computational steps | Captures computational results |
| Dependency-based execution | Dependency-based sharing |
| Rebuilds when inputs change | Remembers what inputs were used |
| Automation focus | Reproducibility focus |
| Rules and targets | Beads and boxes |

**Use together**: Make for automation, Bead for preservation.

```makefile
# Makefile inside a bead
analysis: input/survey.csv
	python analyze.py
	bead save results    # Preserve the completed analysis
```

### Bead vs DVC (Data Version Control)

**Both solve data versioning, but differently.**

| **DVC** | **Bead** |
|---------|----------|
| Git-like interface for data | Computational snapshot approach |
| Tracks data files separately | Packages data + code together |
| Requires git repository | Standalone tool |
| Pipeline definition files | Implicit workflows via dependencies |
| Complex for simple use cases | Simple for complex use cases |

**Choose based on needs**: DVC if you love git workflows, Bead if you want simplicity.

### Bead vs MLflow/Weights & Biases (ML Experiment Tracking)

**MLflow tracks ML experiments. Bead tracks any computational research.**

| **MLflow/W&B** | **Bead** |
|----------------|----------|
| ML model focus | General research focus |
| Metrics and parameters | Complete workflows |
| Web dashboards | File-based simplicity |
| Model registry | Bead boxes |
| Cloud-first | Local-first |

**Use together**: MLflow for ML metrics, Bead for overall reproducibility.

### Bead vs Jupyter Notebooks

**Notebooks mix code and results. Beads separate them cleanly.**

| **Jupyter** | **Bead** |
|-------------|----------|
| Interactive development | Reproducible archiving |
| Code + output in one file | Code and data separate |
| Great for exploration | Great for preservation |
| Version control challenges | Built for versioning |
| Individual analysis | Collaborative workflows |

**Use together**: Jupyter for development, Bead for sharing results.

```bash
# Development cycle
jupyter notebook explore.ipynb    # Interactive exploration
# Convert insights to script
python final_analysis.py         # Clean, reproducible code
bead save analysis-results        # Archive the final version
```

## The Bead Niche: Computational Research Reproducibility

**Bead fills a specific gap**: tracking the relationship between data, code, and results in research workflows.

### What Makes Bead Different

1. **Research-focused**: Built for scientists, analysts, and researchers
2. **Data-centric**: Tracks which data created which results
3. **Collaboration-friendly**: Easy sharing without complex setup
4. **Tool-agnostic**: Works with Python, R, Stata, Julia, anything
5. **Simple**: No servers, databases, or complex configuration

### When to Use Bead

✅ **Perfect for**:
- Multi-step data analysis pipelines
- Research that needs to be reproduced months later
- Team collaboration on computational projects
- Sharing analysis with exact reproducibility
- Tracking data provenance and lineage

❌ **Not the right tool for**:
- Pure software development (use Git)
- Managing software installations (use Conda/Docker)
- Real-time data processing (use workflow engines)
- Web application deployment (use Docker/Kubernetes)

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