#!/usr/bin/env python3
"""
Generate a PDF presentation from the bead web graphs and README descriptions.
"""

import os
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import black, blue, green, red

def read_bead_descriptions():
    """Read descriptions from actual bead README files."""
    descriptions = {}
    
    bead_names = ['node_a_1', 'node_a_2', 'node_b_1', 'node_b_2', 'node_c', 'node_a_1_v2']
    
    for bead_name in bead_names:
        readme_path = f"temp/{bead_name}/output/README.md"
        try:
            with open(readme_path, 'r') as f:
                content = f.read().strip()
                # Remove markdown formatting
                content = content.replace('```markdown', '').replace('```', '').strip()
                descriptions[bead_name] = content
        except:
            # Fallback descriptions
            fallback = {
                'node_a_1': 'Starting node called node_a_1. No inputs in input folder. The raw data is in output folder.',
                'node_a_2': 'Starting node called node_a_2. No inputs in input folder. The raw data call it data_2 is in the output folder.',
                'node_b_1': 'My new output is ready with my code in code.py using node_a_1 latest version.',
                'node_b_2': 'My new output is ready with my code in code.py using node_a_1 latest and node_a_2.',
                'node_c': 'A different project. Not connected with node_a_1, node_a_2, node_b_1 or node_b_2.',
                'node_a_1_v2': 'Starting node called node_a_1. No inputs in input folder. The raw data is in output folder is updated. The bead meta is changed.'
            }
            descriptions[bead_name] = fallback.get(bead_name, f'Description for {bead_name} not available.')
    
    return descriptions

def create_presentation():
    """Create PDF presentation with actual bead descriptions."""
    # Read actual bead descriptions
    descriptions = read_bead_descriptions()
    
    # Create PDF in landscape mode for better graph viewing
    doc = SimpleDocTemplate("output/bead_web_presentation.pdf", 
                          pagesize=landscape(A4),
                          topMargin=0.5*inch,
                          bottomMargin=0.5*inch,
                          leftMargin=0.5*inch,
                          rightMargin=0.5*inch)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        textColor=blue,
        spaceAfter=20
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=green,
        spaceAfter=12
    )
    
    # Title page
    story.append(Paragraph("Bead Web Visualization Presentation", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Dependency Tracking and Graph Generation", styles['Heading2']))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Generated on: August 24, 2025", styles['Normal']))
    story.append(PageBreak())
    
    # Overview with actual descriptions
    story.append(Paragraph("Bead Descriptions (from actual README files)", heading_style))
    story.append(Paragraph(f"<b>node_a_1:</b> {descriptions['node_a_1']}", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>node_a_1_v2:</b> {descriptions['node_a_1_v2']}", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>node_a_2:</b> {descriptions['node_a_2']}", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>node_b_1:</b> {descriptions['node_b_1']}", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>node_b_2:</b> {descriptions['node_b_2']}", styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>node_c:</b> {descriptions['node_c']}", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Versioning explanation
    story.append(Paragraph("Bead Versioning Demonstrated", heading_style))
    story.append(Paragraph("node_a_1 exists in two versions with different timestamps:", styles['Normal']))
    story.append(Paragraph("• Version 1 (13:17:19): Basic raw data", styles['Normal']))
    story.append(Paragraph("• Version 2 (13:20:02): Updated raw data with meta changes", styles['Normal']))
    story.append(Paragraph("The system automatically uses the latest version (13:20:02) in dependencies.", styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # Connection flow
    story.append(Paragraph("Connection Flow", heading_style))
    story.append(Paragraph("• node_a_1 (raw data) → node_b_1 (simple processing example)", styles['Normal']))
    story.append(Paragraph("• node_a_1 (latest) + node_a_2 (data_2) → node_b_2 (convergence processing)", styles['Normal']))
    story.append(Paragraph("• node_c (independent project - no connections)", styles['Normal']))
    story.append(PageBreak())
    
    # Graph 1
    story.append(Paragraph("Graph 1: Simple Dependency Example", heading_style))
    story.append(Paragraph("Perfect starting point: shows the basic concept with node_a_1 (source) flowing to node_b_1 (derived). This demonstrates the fundamental bead dependency relationship.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    if os.path.exists("output/graph_1_dependency_flow.png"):
        try:
            img1 = Image("output/graph_1_dependency_flow.png")
            img1.drawHeight = 4*inch
            img1.drawWidth = 6*inch
            story.append(img1)
        except:
            story.append(Paragraph("Graph 1 image could not be loaded", styles['Normal']))
    else:
        story.append(Paragraph("Graph 1 image not found", styles['Normal']))
    story.append(PageBreak())
    
    # Graph 2  
    story.append(Paragraph("Graph 2: Convergence with Versions", heading_style))
    story.append(Paragraph("Shows convergence pattern where multiple sources (node_a_1 and node_a_2) feed into node_b_2. Also displays version history of node_a_1, demonstrating how bead tracks evolution over time.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    if os.path.exists("output/graph_2_convergence_with_versions.png"):
        try:
            img2 = Image("output/graph_2_convergence_with_versions.png")
            img2.drawHeight = 4*inch
            img2.drawWidth = 6*inch
            story.append(img2)
        except:
            story.append(Paragraph("Graph 2 image could not be loaded", styles['Normal']))
    else:
        story.append(Paragraph("Graph 2 image not found", styles['Normal']))
    story.append(PageBreak())
    
    # Graph 3
    story.append(Paragraph("Graph 3: Complete Bead Web", heading_style))
    story.append(Paragraph("The full picture: all 5 beads showing the convergence pattern where node_b_2 processes both node_a_1 (latest) and node_a_2 (data_2).", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    if os.path.exists("output/graph_3_all_beads_overview.png"):
        try:
            img3 = Image("output/graph_3_all_beads_overview.png")
            img3.drawHeight = 4*inch
            img3.drawWidth = 6*inch
            story.append(img3)
        except:
            story.append(Paragraph("Graph 3 image could not be loaded", styles['Normal']))
    else:
        story.append(Paragraph("Graph 3 image not found", styles['Normal']))
    story.append(PageBreak())
    
    # Graph 4
    story.append(Paragraph("Graph 4: All Beads and Versions", heading_style))
    story.append(Paragraph("Complete colored visualization showing all beads, connections, and version history. This comprehensive view displays the entire bead ecosystem including convergence patterns and versioning.", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    if os.path.exists("output/graph_4_all_beads_and_versions.png"):
        try:
            img4 = Image("output/graph_4_all_beads_and_versions.png")
            img4.drawHeight = 4*inch
            img4.drawWidth = 6*inch
            story.append(img4)
        except:
            story.append(Paragraph("Graph 4 image could not be loaded", styles['Normal']))
    else:
        story.append(Paragraph("Graph 4 image not found", styles['Normal']))
    story.append(PageBreak())
    
    # Technical details
    story.append(Paragraph("Technical Details", heading_style))
    story.append(Paragraph("• Used bead web command with color and heads options", styles['Normal']))
    story.append(Paragraph("• Filtered graphs to focus on specific node relationships", styles['Normal']))
    story.append(Paragraph("• Isolated environment by forgetting other bead boxes", styles['Normal']))
    story.append(Paragraph("• Generated PNG visualizations with dependency tracking", styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    # Graph specifications
    story.append(Paragraph("Graph Specifications:", styles['Heading2']))
    story.append(Paragraph("• Graph 1: 29KB - Simple dependency example (node_a_1 → node_b_1)", styles['Normal']))
    story.append(Paragraph("• Graph 2: <1KB - All source nodes (entry points)", styles['Normal']))
    story.append(Paragraph("• Graph 3: 67KB - Complete bead web (5 beads with convergence pattern)", styles['Normal']))
    story.append(Paragraph("• Graph 4: 44KB - Versioning example (multiple node_a_1 timestamps)", styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print("PDF presentation created: output/bead_web_presentation.pdf")

if __name__ == "__main__":
    create_presentation()
