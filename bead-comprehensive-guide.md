# Bead: Comprehensive Guide to Reproducible Computational Research

**Bead** is a command-line interface (CLI) tool designed to revolutionize how computational research is conducted, shared, and reproduced. Originally developed to address the fundamental challenges of reproducible research computing - questions like "What exact version of the data did we use?" and "How do we reproduce this result?" that researchers face multiple times every day.

Bead implements a paradigm where discrete computations are packaged as self-contained, versioned units called "beads" that follow the fundamental pattern:

```
output = code(*inputs)
```

## Table of Contents

1. [The Problem Bead Solves](#the-problem-bead-solves)
2. [Core Design Principles](#core-design-principles)
3. [What Bead Does and Doesn't Do](#what-bead-does-and-doesnt-do)
4. [Core Concepts and Architecture](#core-concepts-and-architecture)
5. [Common Use Cases](#common-use-cases)
6. [Section 1: Bead Box Management and Basic Operations](#section-1-bead-box-management-and-basic-operations)
7. [Section 2: Dependency Management with Bead Input Commands](#section-2-dependency-management-with-bead-input-commands)
8. [Section 3: Advanced Workflows and Best Practices](#section-3-advanced-workflows-and-best-practices)
9. [Edge Cases and Pitfalls](#edge-cases-and-pitfalls)

---

## The Problem Bead Solves

### The Reproducibility Crisis in Computational Research

Before bead, researchers faced these daily questions:
- **"What version of the data did we use?"**
- **"How do we reproduce this result?"** 
- **"Which code did we run?"**
- **"What happened to our intermediate files?"**

These questions arise **3-5 times every single day** in active research environments, indicating fundamental problems with traditional approaches to computational research. Research by Kandel et al. (2012) identified that tacit knowledge about data is hard to find, efforts are duplicated, communication in diverse teams is sparse, and intermediate steps of analysis are rarely reused.

### Traditional Problems

1. **Version Confusion**: No systematic way to track which version of data was used for specific results
2. **Dependency Hell**: Complex chains of scripts with unclear dependencies
3. **Data Scattered**: Input data, intermediate files, and outputs spread across different locations
4. **Sharing Difficulties**: Hard to package and share complete computational workflows
5. **Reproducibility Failures**: Inability to recreate exact conditions that produced specific results
6. **Tool Fragmentation**: The multitude of software tools and work methods create frictions in the analytics process
7. **Knowledge Loss**: When team members leave, tacit knowledge about data and processes is destroyed

### Bead's Solution

Bead solves these problems by implementing **frozen computation** - each bead is an immutable snapshot of:
- **Exact input data** (identified by content hash)
- **Complete code** (all scripts and dependencies)
- **Generated outputs** (results and artifacts)
- **Metadata** (timestamps, dependencies, provenance)

This creates a **directed acyclic graph (DAG)** of computational dependencies where each node represents a complete, reproducible computation.

---

## Core Design Principles

### 1. **Immutability and Versioning**
- Every bead save creates a **new immutable archive** with timestamp
- **No in-place modifications** - changes create new versions
- **Content-based addressing** ensures exact input matching

### 2. **Language and Tool Agnostic**
- **No assumptions** about programming languages, frameworks, or tools
- **You manage execution** - bead only manages files and dependencies
- **Convention over configuration** - minimal constraints, maximum flexibility
- **Tool independence** - works with any workflow that uses the file system for scripts and data

### 3. **Explicit Dependency Management**
- **Declare all inputs explicitly** via `bead input add`
- **Content hash verification** ensures exact input matching
- **Read-only input protection** prevents accidental data modification

### 4. **Local-First with Distributed Capability**
- **Bead boxes** are simple directory-based storage
- **No central server required** - works completely locally
- **Easy sharing** via file systems, network drives, or manual transfer
- **Supports diverse teams** - accommodates different work methods and tool preferences

### 5. **Human-Readable Archives**
- **Standard zip format** - accessible even without bead tools
- **Clear directory structure** separating code, data, and metadata
- **Emergency access** - researchers can extract and use data manually

---

## What Bead Does and Doesn't Do

### ✅ What Bead DOES:

**File and Dependency Management:**
- Creates immutable snapshots of computational workflows
- Manages input/output dependencies with content verification
- Provides versioned storage in "bead boxes"
- Enables deterministic recreation of computational environments

**Workflow Organization:**
- Enforces clear separation of inputs, outputs, code, and temporary files
- Maintains provenance and lineage tracking
- Supports complex dependency graphs (DAGs)
- Facilitates collaboration through standardized packaging

**Reproducibility Guarantees:**
- Ensures exact input data matching via content hashes
- Preserves complete computational context
- Enables time-travel to previous versions
- Provides audit trails for scientific workflows

### ❌ What Bead DOESN'T Do:

**Execution Management:**
- **Does NOT run your code** - you execute computations manually
- **Does NOT manage software dependencies** - use conda, pip, etc.
- **Does NOT provide job scheduling** - use your preferred job system
- **Does NOT handle parallel processing** - manage this in your scripts

**Data Storage and Sharing:**
- **Does NOT provide cloud storage** - you manage bead box locations
- **Does NOT handle large data optimization** - you choose file formats
- **Does NOT provide access control** - use filesystem permissions
- **Does NOT sync across machines** - you handle distribution

**Development Environment:**
- **Does NOT provide IDE integration** - use your preferred editor
- **Does NOT manage virtual environments** - use conda, venv, etc.
- **Does NOT provide debugging tools** - use language-specific debuggers

### 🎯 The Philosophy: "Bead is Moving Files"

As stated in the demo: *"We ask you to use files because bead is moving files, but that's it."*

Bead is intentionally **minimal and focused** - it manages files and their relationships, leaving everything else to you and your preferred tools. This design makes it:
- **Universally applicable** across all computational domains
- **Non-intrusive** to existing workflows
- **Future-proof** as technologies change
- **Simple to understand** and debug

---

## Core Concepts and Architecture

### What is a Bead?

A bead is fundamentally a **zip archive** that encapsulates a complete computational unit. Each bead contains:

- **Inputs**: References (content_id hashes) to other beads or external data sources
- **Code**: All scripts, programs, and configuration files needed for computation
- **Output**: The results generated by running the code on the inputs
- **Metadata**: Rich information supporting versioning, linking, and distributed workflows

### Bead Archive Structure

When you extract a bead archive as a zip file, you'll find this internal structure:

```
bead-archive.zip
├── code/
│    ├── script1.sh      
│    ├── script2.py
├── meta/
│   ├── bead               # Core metadata (JSON format)
│   ├── input.map          # Input dependency mappings
│   └── manifest           # Complete file manifest with checksums
├── data/
│   ├── data1              # Data from the output folder
│   ├── data2              
```

### Standard Workspace Directory Structure

Every bead workspace follows this conventional layout:

```
workspace/
├── .bead-meta/            # Bead metadata directory
│   ├── bead              # Configuration and dependency info
│   └── input.map         # Input mappings (if any)
├── input/                # Input data (managed by bead)
│   ├── dataset1/         # First input dependency
│   │   ├── README.md
│   │   └── data.csv
│   ├── dataset2/         # Second input dependency  
│   │   ├── README.md
│   │   └── processed.txt
│   └── ...
├── output/               # Final computation outputs
│   ├── README.md         # Documentation of outputs
│   ├── results.csv
│   └── figure.pdf
├── temp/                 # Temporary/intermediate files
│   ├── cache/
│   └── working_files/
├── src/                  # Source code
│   ├── download.sh
│   ├── process.py
│   └── analyze.R
├── Makefile              # Build automation (optional)
└── README.md             # Project documentation
```

---

## Common Use Cases

### 1. **Source Data Beads (Raw Data Collection)**

**Scenario**: You obtain data from external sources (APIs, manual collection, surveys)

**Step-by-Step Workflow**:
```bash
# 1. Create a new workspace for the data source
bead new data-collection-survey

# 2. Navigate to the workspace  
cd data-collection-survey

# 3. Add data files to output/ (since this produces data)
cp /path/to/survey_responses.csv output/
echo "Survey data collected on 2024-01-15" > output/README.md

# 4. Add collection scripts (optional)
mkdir src
echo "#!/bin/bash\n# Script to download survey data\nwget survey-api.com/responses" > src/download.sh

# 5. Save the source bead
bead save data-archive  # data-archive is the name of the bead box where you store your beads
```

**Key Characteristics**:
- **No inputs** - this is a source node in the DAG
- **Data goes in `output/`** - this bead produces data for others to use
- **Always use `-x` flag** when developing source beads
- **Document thoroughly** - others depend on this data

### 2. **Processing Beads (Data Transformation)**

**Scenario**: Transform raw data into analysis-ready format

**Step-by-Step Workflow**:
```bash
# 1. Create processing workspace
bead new data-cleaning

# 2. Navigate to the workspace  
cd data-cleaning

# 3. Add input dependencies
bead input add data-collection-survey  # References the source bead above

# 4. Write processing code
mkdir src
write your code like: src/clean_data.py

# 5. Run the processing
python src/clean_data.py

# 6. Document the processing
echo "Cleaned survey data: removed NaN values" > output/README.md

# 7. Save the processing bead
bead save data-archive  
```

**Key Characteristics**:
- **Has explicit inputs** via `bead input add`
- **Transforms data** from input/ to output/
- **Preserves lineage** - you can trace back to source data
- **Intermediate files** go in temp/ (automatically deleted)

### 3. **Analysis Beads (Sink Nodes)**

**Scenario**: Final analysis that produces reports, figures, papers

**Step-by-Step Workflow**:
```bash
# 1. Create analysis workspace
bead new paper-analysis

# 2. Navigate to the workspace  
cd paper-analysis

# 3. Add all required inputs
bead input add cleaned-survey
bead input add demographic-data
bead input add economic-indicators

# 4. Write analysis code
mkdir src
create your code like: src/analysis.R 

# 5. Run analysis
Rscript src/analysis.R

# 6. Often never save these beads - keep as open workspaces
# Or save occasionally: bead save results  # results is the name of the bead box where you store your beads
```

**Key Characteristics**:
- **Multiple inputs** from various processing beads
- **Often kept as open workspaces** - not saved frequently
- **Final outputs** are consumed by humans (papers, presentations)
- **May use git** for version control within the workspace

### 4. **Human-in-the-Loop Beads**

**Scenario**: Some steps require manual intervention or cannot be fully automated

**Step-by-Step Workflow**:
```bash
# 1. Create workspace for manual processing
bead new manual-coding

# 2. Navigate to the workspace  
cd manual-coding

# 3. Add input data that needs manual review
bead input add interview-transcripts  

# 4. Set up for manual work
mkdir manual_work
cp input/interview-transcripts/*.txt manual_work/

# 5. Perform manual coding/analysis
# (Researcher manually codes interviews over several days)

# 6. Document the manual process
cat > output/coding_methodology.md 

# 7. Save results
cp manual_work/coded_themes.csv output/
bead save results
```

**Key Characteristics**:
- **Documents manual processes** clearly
- **Still maintains provenance** - inputs are tracked
- **Human effort is captured** in the bead archive
- **Reproducible** - others can see exactly what was done

### 5. **Large Data Workflows**

**Scenario**: Working with multi-gigabyte datasets

**Step-by-Step Workflow**:
```bash
# 1. Use efficient data formats
bead new large-data-processing

# 2. Navigate to the workspace  
cd large-data-processing

# 3. Store large data efficiently
# Use parquet, DuckDB, or compressed formats
bead input add large-dataset

# 4. Process in chunks
mkdir src  
cat > src/process_chunks.py 

# 5. Use temp/ for intermediate large files
python src/process_chunks.py  # Creates temp files automatically cleaned

# 6. Keep outputs small and manageable
bead save results
```

**Key Characteristics**:
- **Choose appropriate file formats** (parquet, DuckDB, compressed)
- **Use temp/** for large intermediate files
- **Keep outputs manageable** - aggregate, summarize, filter
- **Performance may not be ideal** due to compression/decompression

---

## Section 1: Bead Box Management and Basic Operations

### Understanding Boxes

**Boxes** are Bead's storage and organization system - think of them as repositories or warehouses where beads are stored and catalogued. Each box is simply a directory path where bead archives are kept, but bead manages the indexing and retrieval automatically.

#### Box Management Commands

##### Adding a New Box

```bash
# Basic syntax
bead box add <box-name> <directory-path>

# Real example from the demo
bead box add demo /Users/yourname/workspace/demo-bead-box
```

**Error Handling**: If the directory doesn't exist, bead will show an error:
```bash
ERROR: /Users/yourname/workspace/demo-bead-box is not an existing directory!
```

**Solution**: Create the directory first:
```bash
mkdir -p /Users/yourname/workspace/demo-bead-box
bead box add demo /Users/yourname/workspace/demo-bead-box
```

##### Listing All Boxes

```bash
bead box list
```

**Example Output**:
```
Boxes:
-------------
cat3: /Volumes/Data3/beadbox
cat2: /Users/yourname/Downloads/beadbox
private: /Volumes/Data3/cat3-bead-box
demo: /Users/yourname/Downloads/workspace/demo-bead-box
```

This shows four different boxes:
- `cat3`: Sensitive data category 3
- `cat2`: Sensitive data category 2
- `private`: Confidential data box
- `demo`: Demo/tutorial box

##### Advanced Box Operations

```bash
# Get detailed help
bead box --help

# Available operations:
bead box add        # Define a box
bead box list       # Show known boxes  
bead box forget     # Remove a box from configuration
bead box rewire     # Remap input dependencies
```

### Creating New Beads and Workspaces

#### Creating a Brand New Bead

```bash
# Create and initialize new workspace directory
bead new <DIRECTORY>

# Examples:
bead new my-analysis
bead new /path/to/new-project
bead new experiment-2025
```

**What `bead new` Does**:
1. **Creates** directory with specified name
2. **Initializes** standard bead structure (`.bead-meta/`, `input/`, `output/`, `temp/`)
3. **Sets up** empty bead metadata
4. **Ready** for development immediately

#### Checking Workspace Status

```bash
# Show current workspace information  
bead status

# Verbose output with detailed information
bead status -v --verbose

# Check specific workspace
bead status --workspace /path/to/workspace
```

**Status Output Includes**:
- Bead name and workspace location
- Input dependencies and their load status
- Timestamp information
- Missing or outdated inputs (with verbose flag)

### Saving Beads

#### Saving Your Current Workspace

```bash
# Save to a specific box
bead save <box-name>

# Example from demo
bead save demo
```

**Success Output**:
```
Successfully stored bead at /Users/yourname/Downloads/workspace/demo-bead-box/paper-analysis_20250730T153158789876+0200.zip.
```

#### Bead Naming Convention

Saved beads follow this timestamp pattern:
```
<project-name>_<YYYYMMDDTHHMMSSSSSSSS><timezone>.zip

Examples:
foreign-cities_20250730T153158789876+0200.zip
paper-analysis_20250730T162143891234+0200.zip
data-processing_20250730T094567123456+0200.zip
```

#### Save Command Options

```bash
# Get detailed help
bead save --help

# Key options:
--workspace DIRECTORY, -w DIRECTORY    # Specify workspace directory
--env DIRECTORY, --environment DIRECTORY    # Environment configuration path
```

**Default Behavior**: If you have exactly one box configured, bead will use it automatically. If you have multiple boxes, you must specify which one to use.

### Opening and Inspecting Existing Beads

#### Method 1: Standard Unzip (Read-Only Inspection)

```bash
# Extract the bead archive for inspection
unzip foreign-cities_20250730T153158789876+0200.zip

# View the contents
tree foreign-cities_20250730T153158789876+0200.zip
```

**Archive Information Display**:
When you unzip, you'll see bead's informational header:
```
Archive:  foreign-cities_20250730T153158789876+0200.zip

This file is a BEAD zip archive.

It is a normal zip file that stores a discrete computation of the form

    output = code(*inputs)

The archive contains

- inputs as part of metadata file: references (content_id) to other BEADs
- code   as files
- output as files
- extra metadata to support
  - linking different versions of the same computation
  - determining the newest version
  - reproducing multi-BEAD computation sequences built by a distributed team

```

#### Method 2: Bead Develop (Active Development)

```bash
# Unpack bead for development (source files only)
bead develop <bead-reference> [target-directory]

# Examples:
bead develop foreign-cities_20250730T153158789876+0200.zip
bead develop foreign-cities_20250730T153158789876+0200.zip my-workspace
bead develop foreign-cities  # Using bead name instead of filename
```

**Bead Develop Options**:
```bash
bead develop --help

Key options:
-t BEAD_TIME, --time BEAD_TIME          # Specify version timestamp
-x, --extract-output                    # Extract output data (normally not needed)
--env DIRECTORY, --environment DIRECTORY    # Environment configuration
```

**What `bead develop` Does**:
1. **Verifies** the archive integrity
2. **Creates** standard workspace directory structure
3. **Extracts** source code to `src/`
4. **Sets up** `.bead-meta/` configuration
5. **Creates** empty `input/`, `output/`, `temp/` directories
6. **Does NOT** extract output data (unless `-x` flag used)

**Example Output**:
```bash
Verifying archive /Users/yourname/Downloads/workspace/demo-bead-box/foreign-cities_20250730T153158789876+0200.zip ...

# Creates workspace structure:
├── .bead-meta/
│   ├── bead
│   └── input.map
├── input/
├── output/
├── temp/
└── src/
    ├── download.sh
    └── filter_east.sh
```

#### When to Use Each Method

**Use Standard Unzip When**:
- Inspecting bead contents without modifying
- Reviewing output data and results
- Do not have the bead program
- Extracting specific files for reference

**Use Bead Develop When**:
- Planning to modify or extend the computation
- Setting up a new development workspace
- Need proper dependency resolution
- Want to re-run the analysis

### Workspace Management

#### Cleaning Up Workspaces

```bash
# Delete entire workspace
bead zap [workspace-directory]

# Examples:
bead zap                    # Delete current directory workspace
bead zap ./my-analysis      # Delete specific workspace
```

**What `bead zap` Does**:
- Completely removes the workspace directory
- Deletes all data, code, and intermediate files
- **WARNING**: This is irreversible - make sure you've saved your important work!

### Advanced Bead Commands

#### Version Information

```bash
# Show bead program version
bead version
```

#### Extended Metadata Export

```bash
# Export extended metadata to file next to zip archive
bead xmeta [workspace-directory]

# This creates a .xmeta file alongside your bead archive
# Useful for external tools that need detailed bead information
```

#### Workspace Verification

```bash
# Check workspace status
tree .bead-meta/
ls -la input/ output/ temp/ src/

# Verify bead configuration
cat .bead-meta/bead
```

### File Transfer Between Boxes

#### Copying Beads Between Boxes

```bash
# Manual copy example from demo:
cp ../demo-bead-box/foreign-cities_20250730T153158789876+0200.zip ./

# This allows you to:
# 1. Move beads between different storage locations
# 2. Share beads via file transfer
# 3. Backup beads to multiple locations
# 4. Distribute beads to team members
```

#### Box-to-Box Workflows

```bash
# Typical workflow:
# 1. Work in local development box
bead save local-dev

# 2. Copy to shared team box  
cp ~/.beadbox/local-dev/analysis_*.zip /shared/team-box/

# 3. Copy to production archive box
cp ~/.beadbox/local-dev/analysis_*.zip /archive/production/
```

---

## Section 2: Dependency Management with Bead Input Commands

### Understanding Input Dependencies

Bead's dependency management system is built around **content-based addressing** - each input is identified by a cryptographic hash of its content, ensuring that dependencies are immutable and precisely versioned.

#### Input Directory Structure

```
workspace/input/
├── dependency1/          # First input dependency
│   ├── README.md         # Documentation of this input
│   ├── data.csv          # Actual input data
│   └── metadata.json     # Additional metadata
├── dependency2/          # Second input dependency
│   ├── README.md
│   └── processed.txt
└── .../                  # Additional dependencies
```

### Complete Input Management Commands

The `bead input` command has six main subcommands for comprehensive dependency management:

```bash
bead input {add,delete,map,update,load,unload}
```

#### Adding New Input Dependencies

```bash
# Add and load data from another bead
bead input add <INPUT-NAME> [BEAD-REF]

# Examples:
bead input add foreign-states                  # Uses foreign-states as bead name
bead input add raw-data /path/to/data.zip       # Uses specific archive file

# Advanced options:
bead input add historical-data --time 20250730T120000000000+0200
```

**What `bead input add` Does**:
1. **Defines** the dependency relationship in `.bead-meta/bead`
2. **Searches** configured boxes for the specified bead
3. **Extracts** output data from the bead to `input/<INPUT-NAME>/`
4. **Creates** input mapping in `.bead-meta/input.map`
5. **Documents** the dependency for future updates

#### Loading Existing Dependencies

```bash
# Load data from already defined dependency
bead input load <input-name>

# Examples:
bead input load foreign-states    # Load previously defined dependency
bead input load --all           # Load all defined but missing inputs
```

**Difference between `add` and `load`**:
- `add`: Define new dependency AND load data
- `load`: Load data from existing dependency definition 

#### Updating Input Dependencies

```bash
# Update specific input to newest version
bead input update <input-name>

# Update to specific version/time
bead input update foreign-states --time 20250730T160000000000+0200

# Update all inputs
bead input update --all

# Examples:
bead input update population-data
bead input update survey-results --time 20250729T090000000000+0200
```

**Update Process**:
1. **Searches** all boxes for newer versions of the input bead
2. **Compares** timestamps and content hashes
3. **Replaces** local input data if newer version found
4. **Updates** `.bead-meta/input.map` with new content_id
5. **Preserves** old data in temporary backup before replacement

#### Remapping Input Sources

```bash
# Change which bead an input loads from
bead input map <input-name> <new-bead-ref>

# Examples:
bead input map foreign-states foreign-states-v2
bead input map test-data production-data
bead input map survey-data /path/to/updated-survey.zip
```

**Use Cases for Remapping**:
- Switch from test data to production data
- Point to corrected version of input data
- Update to renamed bead sources
- A/B testing with different input datasets

#### Unloading Input Data

```bash
# Remove input data but keep dependency definition
bead input unload <input-name>

# Examples:
bead input unload large-dataset    # Free disk space
bead input unload temp-processing  # Remove temporary input
```

**When to Unload**:
- Free disk space for large datasets
- Remove temporary inputs no longer needed
- Clean workspace while preserving dependency definitions

#### Deleting Input Dependencies

```bash
# Completely remove input dependency and data
bead input delete <input-name>

# Examples:
bead input delete deprecated-dataset
bead input delete test-input
```

**Warning**: This completely removes:
- Input data from `input/<input-name>/`
- Dependency definition from `.bead-meta/bead`
- Mapping from `.bead-meta/input.map`

### Advanced Dependency Scenarios

#### Scenario 1: Missing Input Dependencies

**Problem**: You develop a bead but some inputs are not available locally.

```bash
# Error when running analysis:
ERROR: Input 'foreign-states' not found in input/ directory
```

**Solution**:
```bash
# Load the missing input
bead input load foreign-states

# Verify it was loaded
ls input/foreign-states/
# Should show:
# README.md  states.txt
```

#### Scenario 2: Input Version Conflicts

**Problem**: Your analysis depends on a specific version of input data, but a newer version is available.

**Detection**:
```bash
bead input check foreign-states
# Output: New version available: foreign-states_20250730T160000000000+0200.zip
```

**Options**:
```bash
# Option 1: Update to latest version
bead input update foreign-states

# Option 2: Pin to specific version (edit .bead-meta/bead)
# Option 3: Create new bead variant with updated inputs
```

#### Scenario 3: Circular Dependencies

**Problem**: Bead A depends on Bead B, which depends on Bead A.

**Detection**: Bead will detect this during dependency resolution:
```bash
ERROR: Circular dependency detected: A -> B -> A
```

**Solutions**:
1. **Refactor** to break the cycle (recommended)
2. **Create intermediate bead** that both can depend on
3. **Merge** the circular beads into a single computation

#### Scenario 4: Private/Confidential Inputs

**Problem**: Some inputs contain sensitive data that cannot be shared.

**Setup**:
```bash
# Create private box for sensitive data
bead box add private /secure/private-data-box

# Save sensitive analysis to private box
bead save private
```

**Sharing Strategy**:
```bash
# Create public version with synthetic data
bead develop sensitive-analysis_*.zip public-version/
# Replace sensitive inputs with synthetic data
# Save public version
cd public-version 
bead save public
```

#### Scenario 5: External Data Dependencies

**Problem**: Your analysis depends on data from external APIs or databases.

**Pattern**: Create "data ingestion" beads:
```bash
# Create bead for external data fetching
mkdir external-data-fetch/
cd external-data-fetch/
# Create src/fetch.py to download data
# Save as bead
bead save data-sources

# Use in downstream analysis
cd ../main-analysis/
bead input load external-data-fetch
```

### Input Mapping and Rewiring

#### Understanding Input Maps

The `.bead-meta/input.map` file defines how logical input names map to specific bead content IDs:

```json
{
  "foreign-states": "bead-content-id-abc123...",
  "population-data": "bead-content-id-def456...",
  "geographic-boundaries": "bead-content-id-ghi789..."
}
```

#### Rewiring Dependencies

```bash
# Remap an input to a different source bead
bead box rewire <input-name> <new-bead-reference>

# Examples:
bead box rewire foreign-states foreign-states_20250730T170000000000+0200.zip
bead box rewire population-data census-2024
```

**Use Cases for Rewiring**:
1. **Substitute** test data with production data
2. **Update** to corrected versions of input data
3. **Switch** between different data processing variants
4. **A/B testing** with different input datasets

### Dependency Resolution Algorithm

#### Resolution Process

1. **Parse** `.bead-meta/bead` for input requirements
2. **Check** local `input/` directory for existing data
3. **Verify** content hashes match expected values
4. **Search** configured boxes for missing/outdated inputs
5. **Load** required data from matching beads
6. **Update** local input mappings
7. **Validate** all dependencies are satisfied

#### Conflict Resolution

When multiple versions of an input exist:

```bash
# Bead's resolution priority:
# 1. Exact content_id match (highest priority)
# 2. Latest timestamp for same logical name
# 3. User-specified version with --time flag
# 4. Interactive prompt for ambiguous cases
```

#### Performance Optimization

**Caching Strategy**:
- Content-addressed storage prevents duplicate downloads
- Local input directories cache frequently used data
- Box indexing speeds up dependency searches

**Bandwidth Optimization**:
- Only downloads changed portions of large datasets
- Compressed transfer of bead archives
- Incremental updates when possible

### Bead Web Visualization System

Bead includes a powerful web-based visualization system for understanding and managing complex dependency networks across all your beads.

#### Basic Web Visualization

```bash
# Generate basic dependency graph visualization
bead web png dependency-graph.png
bead web svg dependency-graph.svg

# Open visualization in browser
bead web png graph.png view graph.png
```

#### Web Processing Pipeline

The `bead web` command implements a processing pipeline where each subcommand works on an input graph and yields an output graph:

```bash
# Complete pipeline example
bead web \
  / source-bead1 source-bead2 .. sink-bead1 sink-bead2 / \
  heads \
  color \
  png filtered-graph.png \
  view filtered-graph.png
```

#### Web Subcommands Reference

**Graph Loading and Saving**:
```bash
# Load previously saved web metadata
bead web load filename.web png current-state.png

# Save current web metadata for later use
bead web save network-snapshot.web
```

**Filtering and Analysis**:
```bash
# Filter by source and sink relationships
bead web / data-ingestion processing .. analysis reporting /

# Show only most recent computations per cluster
bead web heads png latest-versions.png

# Assign freshness colors (answers: "Are all inputs at latest version?")
bead web color svg freshness-analysis.svg
```

**Dependency Repair and Maintenance**:
```bash
# Auto-repair broken connections (hackish - use with caution)
bead web auto-rewire save repaired.web

# Generate rewiring options file for manual review
bead web rewire-options repair-options.json

# Apply reviewed rewiring options
bead web rewire repair-options.json save fixed-network.web
```

**Visualization Output Formats**:
```bash
# PNG format (good for presentations)
bead web png network-overview.png

# SVG format (scalable, good for documents)  
bead web svg detailed-network.svg

# Open any visualization file in browser
bead web view network-overview.png
```

#### Web Pipeline Use Cases

**Project Health Assessment**:
```bash
# Check if all beads use latest input versions
bead web color png health-check.png view health-check.png
```

**Dependency Impact Analysis**:
```bash
# See what depends on a specific data source
bead web / raw-dataset .. / png impact-analysis.png
```

**Network Cleanup**:
```bash
# Show only actively used beads (remove obsolete versions)
bead web heads color png clean-network.png
```

**Broken Dependency Repair**:
```bash
# Step 1: Identify problems and solutions
bead web rewire-options problems.json

# Step 2: Edit problems.json manually to select preferred solutions

# Step 3: Apply fixes
bead web rewire problems.json png fixed-network.png
```

#### Web Visualization Best Practices

1. **Regular Health Checks**: Use `color` command to identify stale dependencies
2. **Impact Analysis**: Before major changes, use filtering to see affected beads
3. **Cleanup Maintenance**: Use `heads` to focus on current work and identify obsolete beads
4. **Documentation**: Save network snapshots before major reorganizations
5. **Team Coordination**: Share visualizations to communicate project structure

---

## Section 3: Advanced Workflows and Best Practices

### Multi-Project Dependency Workflows

#### Complex Dependency Graph Example

A dependency structure for collecting german-states then creating german-cities combined with other data. 

```
┌─────────────────┐    ┌──────────────────┐
│   german-states │    │   private-data   │
│                 │    │                  │
│ Input: Wikipedia│    │ Input: Confidential│
│ Output: states.txt│  │ Output: filtered_data.dta│
└─────────────────┘    └──────────────────┘
         │                       │
         ▼                       │
┌─────────────────┐              │
│  german-cities  │              │
│                 │              │
│ Input: german-  │              │
│        states   │              │
│ Output: cities.txt│            │
└─────────────────┘              │
         │                       │
         ▼                       ▼
    ┌─────────────────────────────┐
    │          paper              │
    │                             │
    │ Input: german-cities,       │
    │        private-data         │
    │ Output: figure.pdf          │
    └─────────────────────────────┘
```

#### Implementing the Workflow

**Step 1: German States Data Collection**
```bash
mkdir german-states
cd german-states
# Standard bead directory structure created

# Create src/extract_states.py
cat > src/extract_states.py

# Run the extraction
python src/extract_states.py

# Save as bead
bead save demo
```

**Step 2: German Cities Processing** 
```bash
mkdir german-cities
cd german-cities

# Set up dependency on german-states
bead input load german-states

# Create processing scripts
cat > src/download.sh

#!/bin/bash
# Filter cities by East German states using input/german-states/states.txt
grep -f input/german-states/states.txt temp/raw_cities.txt > output/cities.txt

# Execute pipeline
make all  # or bash src/download.sh && bash src/filter_east.sh

# Save processed data
bead save demo
```

**Step 3: Private Data Processing**
```bash
mkdir private-data
cd private-data

# Process confidential data
cat > src/process_confidential.do 

stata -b do src/process_confidential.do

# Save to private box
bead save private
```

**Step 4: Paper Generation**
```bash  
mkdir paper
cd paper

# Load both dependencies
bead input load foreign-cities
bead input load private-data

# Create visualization script
cat > src/plot.sh

# Generate final output
bash src/plot.sh

# Save final paper bead
bead save demo
```

### Team Collaboration Patterns

#### Pattern 1: Distributed Development

**Scenario**: Multiple researchers working on different components of a large analysis.

**Setup**:
```bash
# Each team member has their own development box
bead box add alice-dev /home/alice/bead-workspace
bead box add bob-dev /home/bob/bead-workspace  
bead box add shared-team /shared/team-beads
```

**Workflow**:
```bash
# Alice works on data cleaning
cd alice-analysis/
# ... develop and test ...
bead save alice-dev

# Share with team
cp ~/.bead/alice-dev/data-cleaning_*.zip /shared/team-beads/

# Bob loads Alice's work as input
cd bob-analysis/
bead input load data-cleaning  # Automatically finds Alice's bead
# ... build on Alice's work ...
bead save bob-dev
```

#### Pattern 2: Staged Release Pipeline

**Development → Testing → Production**

```bash
# Development box
bead box add dev /workspace/development
# Testing box  
bead box add test /workspace/testing
# Production box
bead box add prod /workspace/production

# Development workflow
cd my-analysis/
bead save dev

# Promote to testing
cp /workspace/development/analysis_*.zip /workspace/testing/
cd testing-workspace/
bead develop analysis_latest.zip
# Run validation tests
make test
bead save test

# Promote to production
cp /workspace/testing/analysis_*.zip /workspace/production/
```

#### Pattern 3: Fork-and-Merge

**Scenario**: Experimenting with different approaches to the same analysis.

```bash
# Create base analysis
cd base-analysis/
bead save main

# Create experimental fork
bead develop base-analysis_*.zip experiment-v1/
cd experiment-v1/
# Modify approach
bead save experiments

# Create second fork
bead develop base-analysis_*.zip experiment-v2/  
cd experiment-v2/
# Try different approach
bead save experiments

# Compare results and merge best approach back to main
# Manual process - bead doesn't enforce git-like merging
```

### Integration with Existing Tools

#### Integration with Make

**Advanced Makefile Integration**:
```makefile
# Makefile for bead-enabled project
.PHONY: all clean inputs save-bead

# Default target
all: output/results.csv output/figure.pdf

# Ensure inputs are loaded
inputs:
	@echo "Loading input dependencies..."
	@bead input load raw-data || echo "Input raw-data already loaded"
	@bead input load parameters || echo "Input parameters already loaded"

# Main analysis depends on inputs
output/results.csv: inputs src/analyze.py
	python src/analyze.py

# Visualization depends on results
output/figure.pdf: output/results.csv src/plot.R
	Rscript src/plot.R

# Save current state as bead
save-bead: all
	bead save production

# Clean temporary files but preserve inputs and outputs
clean:
	rm -rf temp/*
	
# Nuclear clean - remove everything except source
clean-all:
	rm -rf temp/* output/* input/*
```

#### Integration with Git

**.gitignore for Bead Projects**:
```gitignore
# Bead-specific ignores
input/          # Input data managed by bead
temp/           # Temporary files
*.zip           # Bead archives (store in boxes, not git)

# Keep source and configuration
!src/
!.bead-meta/
!Makefile
!README.md

# Standard ignores
.DS_Store
*.pyc
__pycache__/
.Rhistory
*.log
```

**Git Workflow with Bead**:
```bash
# Initialize git in bead workspace
git init
git add src/ .bead-meta/ Makefile README.md
git commit -m "Initial bead project structure"

# Work on analysis
# ... edit src/analysis.py ...
git add src/analysis.py
git commit -m "Update analysis methodology"

# Save computation state
bead save development

# Both git and bead track different aspects:
# - Git: source code evolution
# - Bead: data dependencies and computational reproducibility
```

#### Integration with Conda/Virtual Environments

**Managing Software Dependencies**:
```bash
# Create environment specification
cat > environment.yml << 'EOF'
name: my-analysis
dependencies:
  - python=3.9
  - pandas
  - matplotlib  
  - pip
  - pip:
    - specialized-package==1.2.3
EOF

# Include in source control
git add environment.yml

# Activate environment before bead operations
conda env create -f environment.yml
conda activate my-analysis
bead develop my-analysis_*.zip
```

### Performance and Scalability

#### Large Dataset Strategies

**Problem**: Working with datasets too large for standard bead archives.

**Solution 1: Data Splitting**
```bash
# Split large dataset into chunks
mkdir data-preparation/
cd data-preparation/
# Create src/split_data.py to chunk large files
# Save splitting logic as bead
bead save data-tools

# Create separate beads for each chunk
for chunk in chunk_*.csv; do
  mkdir "process-${chunk}"
  cd "process-${chunk}"
  ln -s "../${chunk}" input/data.csv
  # Process chunk
  bead save processing
  cd ..
done
```

**Solution 2: External Storage References**
```bash
# Store large data externally, reference in bead
cat > src/load_external.py << 'EOF'
# Reference external storage (S3, network drives, etc.)
import boto3
s3 = boto3.client('s3')
s3.download_file('my-bucket', 'large-dataset.parquet', 'temp/data.parquet')
EOF

# Bead contains logic and metadata, not the large data
```

#### Parallel Processing Workflows

**Multi-Core Processing within Beads**:
```bash
cat > src/parallel_analysis.py << 'EOF'
from multiprocessing import Pool
import pandas as pd

def process_chunk(chunk_id):
    # Process individual chunk
    chunk = pd.read_csv(f'input/data/chunk_{chunk_id}.csv')
    result = chunk.groupby('category').sum()
    return result

# Process all chunks in parallel
with Pool() as pool:
    results = pool.map(process_chunk, range(10))
    
# Combine results
final_result = pd.concat(results)
final_result.to_csv('output/combined_results.csv')
EOF
```

**Multi-Bead Parallel Workflows**:
```bash
# Process multiple beads concurrently
parallel -j 4 "cd {} && make all && bead save batch-processing" ::: analysis_*/

# Or with explicit bead operations
find . -name "*_input.zip" | parallel -j 8 "bead develop {} {/.}_workspace && cd {/.}_workspace && make all && bead save batch-results"
```

### Quality Assurance and Testing

#### Bead Validation Strategies

**Automated Testing Pipeline**:
```bash
cat > src/test_analysis.py << 'EOF'
#!/usr/bin/env python3
import unittest
import pandas as pd
import os

class TestAnalysis(unittest.TestCase):
    def setUp(self):
        # Verify inputs are loaded
        self.assertTrue(os.path.exists('input/raw-data'))
        
    def test_output_exists(self):
        # Run analysis
        os.system('python src/main_analysis.py')
        self.assertTrue(os.path.exists('output/results.csv'))
        
    def test_output_quality(self):
        results = pd.read_csv('output/results.csv')
        # Validate data quality
        self.assertGreater(len(results), 0)
        self.assertFalse(results.isnull().any().any())

if __name__ == '__main__':
    unittest.main()
EOF

# Include testing in Makefile
cat >> Makefile << 'EOF'
test: inputs
	python src/test_analysis.py
	
save-bead: test
	bead save production
EOF
```

#### Reproducibility Verification

**Cross-Platform Testing**:
```bash
# Test bead on different systems
# System 1 (Linux)
bead develop analysis_*.zip test-linux/
cd test-linux && make all

# System 2 (macOS)  
bead develop analysis_*.zip test-macos/
cd test-macos && make all

# Compare outputs
diff test-linux/output/ test-macos/output/
```

**Long-term Reproducibility**:
```bash
# Document software versions in bead
cat > src/environment_snapshot.sh << 'EOF'
#!/bin/bash
echo "=== Software Environment ===" > output/environment.txt
python --version >> output/environment.txt
R --version >> output/environment.txt
conda list >> output/environment.txt
pip freeze >> output/environment.txt
EOF

# Run before main analysis
bash src/environment_snapshot.sh
python src/main_analysis.py
```

### Security and Access Control

#### Sensitive Data Handling

**Private Box Configuration**:
```bash
# Create encrypted private box
mkdir /secure/encrypted-beads
chmod 700 /secure/encrypted-beads
bead box add private-secure /secure/encrypted-beads
```

**Data Sanitization for Sharing**:
```bash
cat > src/create_public_version.py << 'EOF'
#!/usr/bin/env python3
import pandas as pd
import numpy as np

# Load private data
private_data = pd.read_csv('input/confidential/sensitive.csv')

# Create synthetic version preserving statistical properties
public_data = private_data.copy()
# Replace sensitive columns with synthetic data
public_data['personal_id'] = np.random.randint(1000000, 9999999, len(public_data))
public_data['salary'] = np.random.normal(
    private_data['salary'].mean(), 
    private_data['salary'].std(), 
    len(public_data)
)

# Save sanitized version
public_data.to_csv('output/public_data.csv', index=False)
EOF
```

#### Access Audit Trails

**Tracking Bead Usage**:
```bash
cat > src/log_access.py << 'EOF'
#!/usr/bin/env python3
import datetime
import getpass
import socket

# Log access to sensitive bead
with open('temp/access_log.txt', 'a') as f:
    f.write(f"{datetime.datetime.now()}: {getpass.getuser()}@{socket.gethostname()}\n")
EOF

# Include in analysis pipeline
python src/log_access.py
python src/main_analysis.py
```

### Troubleshooting and Recovery

#### Common Issues and Solutions

**Issue 1: Corrupted Bead Archive**
```bash
# Verify bead integrity
unzip -t analysis_*.zip

# If corrupted, restore from backup box
bead box list
cp /backup/bead-box/analysis_*.zip ./
```

**Issue 2: Missing Dependencies**
```bash
# Diagnose missing inputs
cat .bead-meta/bead | grep -A 5 "inputs"

# Search all boxes for missing dependencies
for box in $(bead box list | grep ":" | cut -d: -f1); do
  echo "Searching box: $box"
  find /path/to/$box -name "*dependency-name*"
done
```

**Issue 3: Version Conflicts**
```bash
# Check current input versions
bead input list

# See available versions in boxes
find /path/to/boxes -name "*input-name*" -exec basename {} \;

# Resolve by specifying exact version
bead input load input-name --time 20250730T120000000000+0200
```

#### Disaster Recovery

**Backup Strategy**:
```bash
# Regular backup of all boxes
rsync -av /primary/bead-boxes/ /backup/bead-boxes/

# Export bead index for recovery
bead box list > bead-boxes-backup.txt
```

**Recovery Process**:
```bash
# Restore box configuration
while read line; do
  name=$(echo $line | cut -d: -f1)
  path=$(echo $line | cut -d: -f2 | xargs)
  bead box add $name $path
done < bead-boxes-backup.txt

# Verify recovery
bead box list
```

This comprehensive guide covers the full spectrum of Bead's capabilities, from basic box management to advanced enterprise workflows. The tool's strength lies in its simplicity of concept (discrete computational units) combined with powerful dependency management and sharing capabilities.

## Background and Development

Bead was developed to address fundamental challenges in computational research reproducibility. The tool emerged from research into knowledge flows in organizations, specifically addressing how tacit knowledge about data and computational processes can be preserved and shared effectively. The goal is to translate implicit knowledge about data into explicit, codified knowledge that can be retained and shared across diverse research teams.

Key insights that informed Bead's design:
- Computational data analysis offers unique opportunities to codify tacit knowledge because analysis is performed on machine-readable data using automatable steps
- Much of the tacit knowledge about data can be preserved by encapsulating data, metadata, and dependency references in single packages
- Lightweight, tool-agnostic solutions are more likely to be adopted by diverse teams than rigid, monolithic systems

Bead represents a solution for transparent data analysis that works with diverse teams of researchers and analysts, accommodating different software tools, workflows, and organizational structures. The tool addresses problems identified across both academic research and business analytics environments, where the need for reliable data provenance and reproducible workflows is increasingly critical.

### Training and Accessibility

Bead is designed to be accessible to users with varying technical backgrounds:

**Prerequisites**: 
- Basic familiarity with command-line interfaces (Unix, Mac, or Windows shells)
- No specific programming language requirements - works with Python, R, SQL, Stata, or any language capable of reading and writing files

**Learning Outcomes**:
- Understanding the fundamentals of reproducible research computing
- Ability to create computational chains with multiple interdependent steps
- Skills in dependency management and version control for data workflows

**Accessibility Features**:
- Clear, descriptive error messages and help documentation
- Standard file formats that remain accessible even without Bead tools
- Visual dependency graphs and web-based monitoring tools
- Support for both interactive and automated workflows

---

## Edge Cases and Pitfalls

### 1. **Large Data Handling**

**Issue**: Bead creates copies of data and zips archives, which can be problematic for very large datasets.

**Symptoms**:
- Slow save/load operations
- Excessive disk space usage
- Memory issues during compression

**Solutions**:
```bash
# For large outputs, consider using -x flag sparingly
bead develop -x large-data  # Only when you need to inspect outputs

# Without -x, outputs aren't extracted
bead develop large-data     # Faster for large datasets
```

**Real-world example**: The team successfully works with beads up to 400GB (compressed), but performance considerations apply.

### 2. **Permission Issues with Input Folders**

**Issue**: Input folders are intentionally read-only to prevent data modification.

**Symptoms**:
```bash
$ rm input/data.csv
rm: input/data.csv: Permission denied
```

**Solutions**:
- Use `bead zap` to properly clean up workspaces
- Never try to manually delete input folders
- Accept that input data is immutable by design

### 3. **Git Integration Complexities**

**Issue**: Using git inside beads can create conflicts with bead's internal management.

**Safe practices**:
```bash
# Create .gitignore to exclude bead-managed folders
echo "input/" >> .gitignore
echo "temp/" >> .gitignore
echo "output/" >> .gitignore  # Often excluded
echo ".bead-meta/" >> .gitignore  # Sometimes included for versioning
```

**Advanced usage** (with caution):
```bash
# Version the bead metadata to track input versions
git add .bead-meta/bead
git commit -m "Update to new input data version"
```

**Pitfall**: Never modify `.bead-meta` files through git operations - it can break bead's dependency tracking.

### 4. **Workspace vs Archive Confusion**

**Issue**: Users confuse open workspaces with saved beads.

**Key differences**:
- **Workspace** (open bead): Active directory where you work
- **Archive** (closed bead): Immutable zip file in bead box

**Common mistakes**:
```bash
# Wrong: Trying to share workspace directory
cp -r my-analysis /shared/folder/  # DON'T DO THIS

# Right: Save and share the bead archive
bead save shared-box
# Share the .zip file from the bead box
```

### 5. **Missing or Outdated Dependencies**

**Issue**: Input beads might not be available or have been updated.

**Detection**:
```bash
$ bead input load
ERROR: Cannot find required input 'processed-data' with hash abc123...
```

**Solutions**:
1. Check all bead boxes are mounted:
   ```bash
   bead box list
   ```
2. Update to latest version:
   ```bash
   bead input update
   ```
3. Or revert to previous version:
   ```bash
   bead input update --prev processed-data
   ```

### 6. **Accidental Data in Wrong Folders**

**Issue**: Putting files in wrong folders leads to unexpected behavior.

**Common mistakes**:
- Source data in `temp/` → Lost on save
- Code in `output/` → Treated as data
- Generated files in code folders → Unnecessarily versioned

**Prevention**:
```bash
# Check file placement before saving
tree -d -L 2
# Review what will be saved
ls -la output/
ls -la temp/  # These will be deleted!
```

### 7. **Circular Dependencies**

**Issue**: Creating circular dependencies breaks the DAG requirement.

**Example of what NOT to do**:
```
bead-A depends on bead-B
bead-B depends on bead-C  
bead-C depends on bead-A  # CIRCULAR!
```

**Solution**: Refactor into proper DAG structure, possibly extracting common data into separate source bead.

### 8. **External Data References**

**Issue**: Hard-coded paths to external data break reproducibility.

**Anti-pattern**:
```python
# DON'T DO THIS
data = pd.read_csv("/Users/myname/secret-data/file.csv")
```

**Better approach for unmovable data**:
```makefile
# In source bead that filters/anonymizes external data
output/filtered_data.csv: 
    python filter.py /secure/server/private/data.csv > $@
```

### 9. **Timestamp Precision Issues**

**Issue**: Bead doesn't preserve original file timestamps.

**Impact**: 
- Make-based workflows might rebuild unnecessarily
- Historical timestamp information is lost

**Workaround**: Store important timestamps in metadata files if needed.

### 10. **Storage Management**

**Issue**: Multiple versions accumulate quickly, consuming disk space.

**Symptoms**:
```bash
$ ls demo-box/ | wc -l
247  # Too many versions!
```

**Solutions**:
1. Use archival scripts to move old versions
2. Implement retention policies
3. Use different boxes for different lifecycle stages

### 11. **Human-in-the-Loop Pitfalls**

**Issue**: Manual steps break full automation.

**Best practices**:
- Document manual steps clearly in README
- Use clear naming: `manual-review-needed/`
- Consider semi-automation where possible

### 12. **Common Command Mistakes**

**Forgetting -x flag**:
```bash
# Mistake: Wondering where outputs went
bead develop my-data
ls output/  # Empty!

# Fix: Use -x for data beads
bead develop -x my-data
```

**Wrong bead reference**:
```bash
# Mistake: Using full path
bead develop /path/to/beadbox/mybead_20241201.zip

# Better: Use short name
bead develop mybead

# Or specific version
bead develop mybead_20241201.zip
```

**Not checking what will be saved**:
```bash
# Always review before saving
find . -type f -size +100M  # Large files?
ls temp/  # Will be deleted!
ls output/  # Will be shared!
```

### 13. **Analysis Bead Anti-Patterns**

**Issue**: Never saving analysis beads (sink beads) can lose important state.

**Problem scenario**:
- Working on paper/analysis for months
- Never use `bead save`
- Risk losing dependency version information

**Better approach**:
```bash
# Save periodically even if not sharing
bead save analysis-checkpoint

# Use git for fine-grained version control
git add src/ .bead-meta/
git commit -m "Update analysis with new methodology"
```

### 14. **Bead Box Management Issues**

**Forgetting box locations**:
```bash
# Document your box setup
cat > ~/.bead-boxes.md << 'EOF'
# My Bead Box Configuration
- local: ~/bead-boxes/local (development)
- shared: /network/team/beads (collaboration)
- archive: /backup/bead-archive (long-term storage)
- private: /encrypted/private-beads (sensitive data)
EOF
```

**Box naming conflicts**:
```bash
# Avoid generic names
bead box add data ~/boxes  # Too generic!

# Use descriptive names
bead box add project-x-dev ~/project-x/dev-beads
bead box add project-x-prod ~/project-x/prod-beads
```

### 15. **Content Hash Verification Failures**

**Issue**: Modified files outside bead's control can cause hash mismatches.

**Symptoms**:
```
ERROR: Content hash mismatch for input 'processed-data'
Expected: abc123...
Got: def456...
```

**Causes and solutions**:
1. Manual file modification - never edit input files directly
2. Filesystem corruption - verify disk integrity
3. Transfer errors - re-download from source box

These edge cases and pitfalls represent real-world challenges encountered by the bead community. Understanding them helps ensure smooth adoption and effective use of bead for reproducible computational research.