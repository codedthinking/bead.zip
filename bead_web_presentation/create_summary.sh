#!/bin/bash
# Simple script to create a text-based presentation summary

echo "Creating presentation summary..."

cat > output/presentation_summary.txt << 'EOF'
BEAD WEB VISUALIZATION PRESENTATION
==================================

Generated on: August 24, 2025

OVERVIEW
--------
This presentation demonstrates bead dependency tracking using visual graphs.
- 2 source nodes (node_a): Raw data inputs  
- 2 derived nodes (node_b): Processed outputs

CONNECTION FLOW
--------------
node_a_1 (raw data) ────────→ node_b_1 (processed output)
node_a_2 (updated raw) ─────→ node_b_2 (updated output)

BEAD DESCRIPTIONS
----------------
• node_a_1: "Starting node called node A. No inputs. Imagine as raw data."
• node_a_2: "Bead starting node changed. Call it node A_version_2. No inputs. Imagine as raw data updated."  
• node_b_1: "My new output is ready with my code using node_a."
• node_b_2: "My new output is ready with my code using node_a_updated input."

GENERATED GRAPHS
---------------
1. Graph 1: Node A Sources (graph_1_node_a_only.png)
   - Size: 67KB
   - Filter: / node_a .. /
   - Shows only source nodes

2. Graph 2: Node A to B Connections (graph_2_node_a_to_node_b.png)  
   - Size: 28KB
   - Filter: / node_a .. node_b /
   - Shows complete dependency chain

3. Graph 3: All Node Connections (graph_3_all_node_connections.png)
   - Size: 67KB  
   - Filter: / node_a node_b .. /
   - Shows complete network view

TECHNICAL DETAILS
----------------
Commands Used:
• bead develop -x - Extract bead archives
• bead save graph - Save beads to local box
• bead web - Generate visualizations with color and heads
• bead box forget - Remove other boxes for clean view

Environment Setup:
• Forgot boxes: latest, private, ss, skill, proc, people, palturai
• Result: Clean visualization with only 9 beads vs 144+ system beads

CONCLUSION
----------
Successfully demonstrates:
✓ Clear dependency tracking from raw data to processed outputs
✓ Version management with multiple inputs and outputs  
✓ Visual representation with color-coded graphs
✓ Isolated environment for focused visualizations

This enables effective data lineage tracking and pipeline visualization.
EOF

echo "Text summary created: output/presentation_summary.txt"
echo ""
echo "Files created:"
echo "- output/presentation.html (HTML presentation)"
echo "- output/presentation_summary.txt (Text summary)"
echo "- output/graph_1_node_a_only.png"
echo "- output/graph_2_node_a_to_node_b.png"  
echo "- output/graph_3_all_node_connections.png"
echo ""
echo "To view HTML presentation:"
echo "firefox output/presentation.html"
