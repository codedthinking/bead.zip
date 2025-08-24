# Bead Web Presentation

## Overview
This project demonstrates bead dependency tracking and visualization using the bead web command with color and heads options. We now have 6 beads including versioning examples, showing connected workflows, independent projects, and bead evolution over time.

## Bead Structure

### Primary Processing Chain

#### Node A (Source Nodes with Versioning)
- **node_a_1**: Starting node with raw data (no inputs)
  - **Version 1** (13:17:19): "Starting node called node_a_1. No inputs in input folder. The raw data is in output folder."
  - **Version 2** (13:20:02): "Starting node called node_a_1. No inputs in input folder. The raw data is in output folder is updated. The bead meta is changed."

- **node_a_2**: Updated version of raw data (no inputs)  
  - Description: "Starting node called node_a_2. No inputs in input folder. The raw data call it data_2 is in the output folder."

#### Node B (Derived Nodes)
- **node_b_1**: Processes node_a_1 data
  - Input: node_a_1 (latest version)
  - Description: "My new output is ready with my code in code.py using node_a_1 latest version."

- **node_b_2**: Processes BOTH node_a_1 AND node_a_2 data
  - Inputs: node_a_1 (latest) and node_a_2 (convergence node)
  - Description: "My new output is ready with my code in code.py using node_a_1 latest and node_a_2."

### Independent Project
- **node_c**: Standalone project (no inputs, no connections)
  - Description: "A different project. Not connected with node_a_1, node_a_2, node_b_1 or node_b_2."

## Connection Flow

```
Enhanced Structure with Versioning:
node_a_1 v1 (13:17:19) ──────→ [available but not used]
node_a_1 v2 (13:20:02) ──────→ node_b_1 (simple example: Graph 1)
                         ╲
                          ╲
                           ├──→ node_b_2 (convergence: latest node_a_1 + node_a_2)  
                          ╱
                         ╱
node_a_2 (data_2) ──────╱

Independent:
node_c (standalone project)
```

## Bead Versioning Demonstrated

This presentation showcases **bead versioning** - a key feature where multiple versions of the same logical bead can coexist:

- **Same Name, Different Content**: Both node_a_1 versions have identical names but different timestamps and content
- **Automatic Selection**: The bead system automatically uses the latest version (13:20:02) in dependency resolution
- **Version History**: Earlier versions (13:17:19) remain available for comparison and rollback
- **Content Evolution**: Shows how data and metadata evolve over time within the same bead

## Generated Graphs

### Graph 1: Simple Dependency Example (`graph_1_dependency_flow.png`)
- **Size**: 29KB (shows clear node_a_1 → node_b_1 relationship)
- **Purpose**: Demonstrate basic dependency flow with specific example
- **Filter**: `/ node_a_1 .. node_b_1 /`
- **Shows**: Simple chain from node_a_1 (source) to node_b_1 (derived)

### Graph 2: Convergence with Versions (`graph_2_convergence_with_versions.png`)
- **Size**: 58KB (shows full convergence pattern with versioning)
- **Purpose**: Demonstrate convergence where multiple inputs feed into one node, including version history
- **Filter**: `/ .. node_b_2 /`
- **Shows**: Both node_a_1 and node_a_2 converging into node_b_2, plus old version of node_a_1

### Graph 3: Complete Bead Web (`graph_3_all_beads_overview.png`)
- **Size**: 67KB  
- **Purpose**: Show all beads and relationships
- **Filter**: None (shows everything)
- **Shows**: Complete network including convergence node pattern

### Graph 4: All Beads and Versions (`graph_4_all_beads_and_versions.png`)
- **Size**: 86KB (comprehensive colored visualization)
- **Purpose**: Complete overview showing all beads, connections, and version history
- **Filter**: None (shows everything with color)
- **Shows**: Entire bead ecosystem with convergence patterns, versioning, and colored visualization

## Technical Details

### Commands Used
- `bead develop -x` - Extract bead archives for development
- `bead save graph` - Save beads to local graph box
- `bead web` - Generate web visualizations with color and heads options
- `bead box forget` - Remove other boxes to focus on local beads

### Bead Metadata
Each bead contains:
- Freeze name and timestamp
- Input dependencies with content IDs
- Kind identifiers for bead types
- Meta version for compatibility

## Key Features Demonstrated

1. **Dependency Tracking**: Clear lineage from raw data to processed outputs
2. **Version Management**: Multiple versions of inputs with corresponding outputs  
3. **Bead Versioning**: Same logical bead with different timestamps and content evolution
4. **Convergence Patterns**: Single bead processing multiple inputs (node_b_2)
5. **Independent Projects**: Standalone beads not connected to main flow
6. **Visual Representation**: Color-coded graphs showing freshness and connections
7. **Isolated Environment**: Clean visualization focusing only on relevant beads
8. **Automatic Version Selection**: System uses latest version in dependency resolution

## Usage

Run `make graphs` to generate all visualizations or use individual targets:
- `make graph1` - Generate dependency flow graph
- `make graph2` - Generate source nodes graph  
- `make graph3` - Generate complete overview graph
- `make graph4` - Generate versioning example graph
- `make restore-boxes` - Restore all original bead boxes after presentation

The Makefile automatically forgets other bead boxes to ensure clean, focused visualizations.

## Current Status
- **Total Bead Files**: 6 (including 2 versions of node_a_1)
- **Unique Logical Beads**: 5 (node_a_1, node_a_2, node_b_1, node_b_2, node_c)
- **Versioning Example**: node_a_1 has 2 timestamps showing evolution
- **Connected Chain**: 4 beads with convergence pattern (latest node_a_1 + node_a_2 → node_b_2)
- **Independent**: 1 bead (node_c)
- **Graphs Generated**: 4 focused visualizations including version comparison
