# Bead Web Presentation Makefile

.PHONY: clean-graphs setup graphs graph1 graph2 graph3 graph4 all forget-others restore-boxes

# Temporarily forget other boxes for clean graph generation
forget-others:
	@echo "Temporarily forgetting other boxes for clean graph generation..."
	@for box in latest old private ss skill proc kti palturai eu_funds whoiswho people; do \
		bead box forget $$box 2>/dev/null || true; \
	done

# Clean existing graph outputs
clean-graphs:
	rm -f output/*.png output/*.svg

# Setup: forget latest box and ensure output directory exists
# Setup: forget other boxes and ensure output directory exists
setup: forget-others
	mkdir -p output

# Generate individual graphs (using only local graph box)
graph1: setup
	bead web / node_a_1 .. node_b_1 / heads color png output/graph_1_dependency_flow.png

graph2: setup
	bead web / .. node_b_2 / color png output/graph_2_convergence_with_versions.png

graph3: setup
	bead web heads color png output/graph_3_all_beads_overview.png

graph4: setup
	bead web color png output/graph_4_all_beads_and_versions.png

# Generate all graphs and restore boxes
graphs: graph1 graph2 graph3 graph4
	@echo "Graphs generated successfully, restoring bead boxes..."
	@$(MAKE) restore-boxes

# Create presentation
presentation: graphs
	python create_pdf.py
	@echo "PDF presentation created: output/bead_web_presentation.pdf"

# Default target
all: presentation

# List generated files
list:
	ls -la output/

# View presentation in browser
view: presentation
	@echo "To view the presentation, run:"
	@echo "firefox output/presentation.html"

# Restore all bead boxes
restore-boxes:
	bead box add latest /srv/bead-box/latest
	bead box add old /srv/bead-box/archive
	bead box add private /srv/project/balance/data/private_box
	bead box add ss /srv/bead-box/project/supplier_survey
	bead box add skill /srv/bead-box/project/skill_survey
	bead box add proc /srv/bead-box/project/kozbeszerzes
	bead box add kti /srv/project/krtk/bead-box
	bead box add palturai /srv/project/palturai/bead-box
	bead box add eu_funds /srv/project/eu_funds/bead-box
	bead box add whoiswho /srv/project/whoiswho/bead-box
	bead box add people /srv/project/people/bead-box
