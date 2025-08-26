---
title: Related Tools and Alternatives
description: Comparison of bead with other reproducible research tools
order: 6
---

# Related Tools and Alternatives

While bead provides a powerful approach to reproducible research, several other tools address similar challenges with different philosophies and implementations. This guide helps you understand when to use bead versus alternatives.

## Quick Comparison

| Tool | Best For | Language | Approach |
|------|----------|----------|----------|
| **bead** (e3krisztian) | Multi-language pipelines | Python CLI | Explicit dependencies, ZIP archives |
| **orderly2** | R-focused research | R | Automated R workflows, git-like |
| **packit** | Result sharing & web access | Web app | User-friendly interface for outpack data |

## orderly2 vs bead

**Use orderly2 when**:
- Your team primarily uses R
- You want automated report generation
- You need git-like distributed workflows
- You're doing epidemiological/health research

**Use bead when**:
- You use multiple programming languages
- You want explicit control over dependencies
- You prefer manual execution with managed inputs
- You need simple, cross-platform deployment

### Technical Differences

```bash
# orderly2 (R-focused)
orderly2::orderly_init()
orderly2::orderly_run("analysis")

# bead (language-agnostic)
bead new analysis
bead input add clean-data
# run your scripts in any language
bead save results
```

## packit vs bead

**packit** is complementary to bead rather than alternative - it provides a web interface for accessing research outputs.

**Use packit when**:
- You need to share results with non-technical users
- You want web-based authentication and permissions
- You need centralized data management
- You want to browse and discover research outputs

**Use bead when**:
- You're focused on computation management
- You prefer command-line workflows
- You want tool-agnostic dependency management

### Integration Potential

While bead and packit use different formats, they address different parts of the research workflow:

```
[Data Sources] → [bead computation] → [Results] → [packit sharing]
```

## Migration Considerations

### From bead to orderly2
- Convert ZIP archives to outpack format
- Translate dependency declarations to R syntax
- Adapt manual execution to R-automated workflows

### From orderly2 to bead
- Extract computation logic from R scripts
- Declare dependencies explicitly via `bead input add`
- Adapt to manual execution model

### Adding packit to existing workflows
- packit can surface results from either bead or orderly2
- Requires format conversion to outpack standard
- Provides web layer without changing computation tools

## Ecosystem Integration

### R Ecosystem
- **orderly2**: Native R package integration
- **bead**: Works with R scripts but no special integration
- **packit**: Can surface R-generated results

### Python Ecosystem
- **bead**: Python CLI with language-agnostic execution
- **orderly2**: Limited Python support
- **packit**: Can surface Python-generated results

### Multi-language Projects
- **bead**: Designed for multi-language workflows
- **orderly2**: Primarily R, limited multi-language support
- **packit**: Language-agnostic result presentation

## Choosing the Right Tool

### Decision Matrix

1. **Language Requirements**
   - R-only → orderly2
   - Multi-language → bead
   - Any (for sharing) → packit

2. **Execution Model Preference**
   - Automated → orderly2
   - Manual control → bead
   - Web-based → packit

3. **Team Technical Level**
   - R developers → orderly2
   - Mixed technical → bead
   - Including non-technical → packit

4. **Sharing Requirements**
   - Internal R team → orderly2
   - Technical team → bead
   - Broad audience → packit

### Hybrid Approaches

Many successful research teams use combinations:

```
Research Pipeline:
├── Data processing (bead for multi-language)
├── Statistical analysis (orderly2 for R)
└── Result sharing (packit for web access)
```

## Getting Started with Alternatives

### orderly2
```r
install.packages("orderly2", 
  repos = c("https://mrc-ide.r-universe.dev", 
            "https://cloud.r-project.org"))
```

### packit
See [packit documentation](https://github.com/mrc-ide/packit) for web application setup.

## Further Reading

- [Full tool comparison](../tool-comparison.md) - Detailed analysis of all tools
- [orderly2 documentation](https://mrc-ide.github.io/orderly2/)
- [packit repository](https://github.com/mrc-ide/packit)
- [bead concepts](concepts.md) - Core bead principles that inform tool choice