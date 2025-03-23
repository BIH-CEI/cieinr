# Custom Badges and Compatibility Information

## Python Compatibility

[![Python 3.10-3.12](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)

This project is compatible with Python versions 3.10, 3.11, and 3.12. 

**Note on Python 3.13 Incompatibility:**
Due to internal changes in Python 3.13's `dataclasses` module, the LinkML library (a core dependency) is not currently compatible with Python 3.13. Specifically:

1. The LinkML library relies on internal implementation details of `dataclasses` like `_create_fn` which were removed in Python 3.13.
2. Python 3.13 modified how Field objects are passed to internal functions in `dataclasses`.

We've specifically restricted the project to Python < 3.13 in our `pyproject.toml` file to avoid these compatibility issues. If you need to use Python 3.13, consider using Docker with Python 3.12 as described in our documentation.

## LinkML Compatibility

[![LinkML](https://img.shields.io/badge/LinkML-1.8.0+-green.svg)](https://linkml.io/)

This project uses LinkML version 1.8.0 or higher. The LinkML dependency is used for:

1. Schema definition in YAML format
2. Generation of Python data classes
3. Validation of data against the schema
4. Data transformations and conversions

## GA4GH Phenopackets Compatibility 

[![Phenopackets](https://img.shields.io/badge/Phenopackets-2.0-purple.svg)](https://phenopacket-schema.readthedocs.io/en/latest/)

We implement GA4GH Phenopackets schema version 2.0, which provides a standardized format for sharing phenotypic information for a variety of use cases.

## Generate LinkML Python Classes

If you're using Python 3.10-3.12, you can generate Python classes directly:

```bash
gen-python src/cieinr/v1_0_0/linkml_schemas/cieinr.yaml > src/cieinr/v1_0_0/python_schemas/cieinr.py
```

For Python 3.13 users, use our Docker-based approach:

```bash
./generate_linkml.sh
```

## Dynamic Badges
You can create custom badges such as [![LOCs](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/frehburg/25d4f4d4d222fcb5f266a280b1dd60d4/raw/phenopacket_mapper_locs.JSON)](https://github.com/bih-cei/phenopacket_mapper/actions/workflows/locs.yml).

This relies on a GitHub workflow such as:

```
name: Count LOC in Python Files

on:
  push:
    branches: [ develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  count-loc:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Count Total Lines of Code in Python Files
        id: loc  # Give this step an ID to reference later
        run: |
          echo "Counting total lines of Python code..."
          LOC_COUNT=$(git ls-files '*.py' | xargs wc -l | tail -n 1)
          echo "LOC_COUNT=${LOC_COUNT}" >> $GITHUB_ENV
          echo "Python Lines of Code (LOC): $LOC_COUNT"

      - name: Post LOC Count as PR Comment (Only for Main Branch)
        if: github.event_name == 'pull_request' && github.base_ref == 'main'
        uses: peter-evans/create-or-update-comment@v3
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          issue-number: ${{ github.event.pull_request.number }}
          body: |
            ### Python Lines of Code (LOC) Summary
            Total lines of Python code in this repository:
            ```
            ${{ env.LOC_COUNT }}
            ```

      - name: Create Awesome Badge
        uses: schneegans/dynamic-badges-action@v1.7.0
        with:
          auth: ${{ secrets.GIST_SECRET }}
          gistID: 25d4f4d4d222fcb5f266a280b1dd60d4
          filename: phenopacket_mapper_locs.JSON # Use test.svg if you want to use the SVG mode.
          label: Lines of Code
          message: ${{ env.LOC_COUNT }}
          color: blue
```

You can see the last section on creating a badge. In order for this to work, you need to follow the steps in this tutorial: [Dynamic Badges Action](https://github.com/marketplace/actions/dynamic-badges)

TLDR:

1. Create a gist file (e.g., `test.json`) at https://gist.github.com/.
2. Create a GitHub Access token with the Gist access.
3. Create a secret in your repository and call it `GIST_SECRET`
4. Configure the workflow to write to the gist as seen above
5. Add the badge to your README like this:
```
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/<user>/<gist-ID>/raw/test.json)
```
