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


## Best Practices

### 1. Descriptive Input Names

```bash
# Match input name to source bead
$ bead input add customer-demographics

# Clear names in code
demographics = pd.read_csv('input/customer-demographics/data.csv')
```

### 2. Document Dependencies

In your README:
```markdown
## Dependencies

This bead requires:
- `survey-responses`: Raw survey data (v2024-07-30 or later)
- `census-data`: Population statistics for weighting
```

### 3. Test with Different Versions

```bash
# Test with latest
$ bead input update
$ make test

# Test with production version
$ bead input map survey-data survey-data_20250701T000000+0200.zip
$ make test
```

### 4. Handle Missing Inputs Gracefully

```python
import os
import sys

required_inputs = ['survey-data', 'model-parameters']
for inp in required_inputs:
    if not os.path.exists(f'input/{inp}'):
        print(f"ERROR: Required input '{inp}' not loaded")
        print(f"Run: bead input load {inp}")
        sys.exit(1)
```

## Advanced Patterns

### Conditional Dependencies

```python
# config.json specifies which inputs to use
config = json.load(open('config.json'))

if config['use_external_data']:
    if not os.path.exists('input/external-source'):
        raise ValueError("External data not loaded")
    external = pd.read_csv('input/external-source/data.csv')
```

### Dependency Versioning in Analysis

Track which versions produced results:

```python
# Record input versions in output
import os
import json

versions = {}
for input_dir in os.listdir('input'):
    # Get version from symlink or metadata
    versions[input_dir] = get_input_version(input_dir)

with open('output/input-versions.json', 'w') as f:
    json.dump(versions, f, indent=2)
```

### Multi-Stage Processing

```bash
# Stage 1: Quick prototype with subset
$ bead input add data-subset
$ python prototype.py
$ bead save prototype

# Stage 2: Full analysis with complete data  
$ bead input delete data-subset
$ bead input add data-complete
$ python full_analysis.py
$ bead save final
```
