#set page(
  paper: "a4",
  flipped: true,
  margin: (x: 1.5cm, y: 1.5cm),
  fill: white,
)

#set text(
  font: ("Helvetica Neue", "Arial", "sans-serif"),
  size: 8.5pt,
  fill: rgb("#232324"),
)

#set par(
  justify: false,
  leading: 0.52em,
)

#let brand-red = rgb("#E61E25")
#let secondary = rgb("#5D5A88")
#let text-muted = rgb("#5D5A88")
#let border-color = rgb("#D4D2E3")
#let code-bg = rgb("#D4D2E3")
#let bg-alt = rgb("#f8fafc")

#let rounded-box(title: none, content, fill: white) = {
  block(
    fill: fill,
    stroke: 1pt + border-color,
    radius: 6pt,
    inset: 10pt,
    width: 100%,
    {
      if title != none {
        text(size: 10pt, weight: 700, fill: brand-red)[#title]
        v(6pt)
      }
      content
    }
  )
}

#let code-block(content) = {
  block(
    fill: code-bg,
    radius: 4pt,
    inset: 6pt,
    width: 100%,
    raw(content, lang: "bash")
  )
}

#let section-heading(content) = {
  text(size: 11pt, weight: 700, fill: brand-red)[#content]
  v(4pt)
}

// Title
#align(center)[
  #text(size: 24pt, weight: 700, fill: brand-red)[bead cheatsheet]
  #v(2pt)
  #text(size: 10pt, fill: text-muted)[Create a workspace, declare explicit inputs, write outputs, save an immutable archive (.zip) into a box.]
]

#v(8pt)

// Main content in 3 columns
#columns(3, gutter: 12pt)[

// Column 1: Folder structure and common workflows
#rounded-box(title: "Folder Roles")[
  #text(weight: 600)[`input/`] — Dependencies from upstream beads (read-only)\
  #text(weight: 600)[`output/`] — Results to share with downstream beads\
  #text(weight: 600)[`temp/`] — Scratch files; cleared when saving\
  #text(weight: 600)[`.bead-meta/`] — Internal metadata; do not edit\
  #text(weight: 600)[Everything else] — Your code, notebooks, docs
]

#v(8pt)

#section-heading[Most Common Workflows]

#rounded-box(title: "1. Start a new workspace")[
  #code-block("$ bead new my-analysis
$ cd my-analysis")
  • Put code in your own folders\
  • Write final results to `output/`
]

#rounded-box(title: "2. Use another bead as input")[
  #code-block("$ bead input add raw-survey-data
$ ls input/raw-survey-data/")
  • Use relative paths from `input/<name>/`\
  • To free space later:
  #code-block("$ bead input unload raw-survey-data")
]

#rounded-box(title: "3. Update when upstream changes")[
  #code-block("$ bead input update")
  Pulls the latest versions of all declared inputs
]

// Column 2: Save, reopen, and best practices
#rounded-box(title: "4. Save immutable archive to box")[
  #code-block("$ bead box add my-beads ~/bead-storage
$ bead save my-beads")
  • Produces timestamped .zip in the box\
  • Anyone can open .zip without bead installed
]

#rounded-box(title: "5. Reopen or review saved bead")[
  #code-block("$ bead edit <ref>
$ bead edit --review <ref>")
  • `<ref>` can be name, path, or identifier\
  • `--review` mounts outputs for review only
]

#rounded-box(title: "6. Discard workspace")[
  #code-block("$ bead discard")
  Safe to remove; deletes current workspace
]

#v(8pt)

#section-heading[What Goes Where]

#rounded-box(fill: bg-alt)[
  • #text(weight: 600)[Final deliverables:] write to `output/`\
  • #text(weight: 600)[Large intermediates:] keep in `temp/`\
  • #text(weight: 600)[Never write to] `input/` (managed by bead)\
  • #text(weight: 600)[Include] a short `output/README.md`
]

#v(8pt)

#section-heading[Language-Agnostic Usage]

#rounded-box(fill: bg-alt)[
  • Run any tool (bash, Python, R, Stata, Julia, SQL)\
  • Use relative paths; avoid absolute paths\
  • Capture environment info alongside outputs\
    (e.g., `requirements.txt`, `Project.toml`)
]

// Column 3: Commands reference and patterns
#section-heading[Key Commands]

#rounded-box(title: "Workspaces", fill: bg-alt)[
  #raw("bead new <name>           # create workspace
bead edit <ref>           # recreate from saved
bead edit --review <ref>  # open for review
bead save <box>           # save .zip to box
bead discard              # delete workspace", lang: "bash")
]

#rounded-box(title: "Inputs (dependencies)", fill: bg-alt)[
  #raw("bead input add <name>     # declare & load
bead input load <name>    # load declared
bead input update         # update all inputs
bead input unload <name>  # free disk space", lang: "bash")
]

#rounded-box(title: "Boxes (storage)", fill: bg-alt)[
  #raw("bead box add <name> <path>  # register box
bead box list               # list boxes
bead box forget <name>      # remove reference", lang: "bash")
]

#v(8pt)

#section-heading[Quick Patterns]

#rounded-box(title: "Chain of provenance (A → B → C)")[
  #raw("$ bead new raw-data
# write to output/...
$ bead save my-beads

$ bead new clean-data
$ bead input add raw-data
# read input/raw-data/, write output/
$ bead save my-beads

$ bead new final-analysis
$ bead input add clean-data
# read input/clean-data/, write output/
$ bead save my-beads", lang: "bash")
]

#rounded-box(fill: bg-alt)[
  #text(size: 7.5pt, fill: text-muted, style: "italic")[
    bead gives you immutable snapshots, explicit inputs, and a clear chain of provenance—so results are reproducible and sharable beyond tomorrow.
  ]
]

]