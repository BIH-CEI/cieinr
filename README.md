# Canadian Inborn Errors of Immunity National Registry (CIEINR) Data Model

[![Python 3.10-3.12](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)
[![License: Apache v2.0](https://img.shields.io/badge/License-Apache2.0-yellow.svg)](https://opensource.org/licenses/MIT)
[![Phenopackets](https://img.shields.io/badge/Phenopackets-2.0-purple.svg)](https://phenopacket-schema.readthedocs.io/en/latest/)
[![LinkML](https://img.shields.io/badge/LinkML-1.8.0+-green.svg)](https://linkml.io/)
[![RareLink](https://img.shields.io/badge/RareLink-v2.0.0-blue.svg)](https://github.com/BIH-CEI/RareLink)

This repository houses the LinkML representation of the data model for
the Canadian Inborn Errors of Immunity National Registry (CIEINR) and its
all configurations for instant export to GA4GH Phenopackets utilising the 
RareLink v2.0.0.dev1 engine.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
- [Usage](#usage)
   - [Importing from RareLink](#importing-from-rarelink)
   - [Generating Phenopackets](#generating-phenopackets)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

The Canadian Inborn Errors of Immunity National Registry (CIEINR) aims
to collect and standardize data on patients with inborn errors of
immunity (IEI) across Canada via REDCap. This repository provides the LinkML
representation of the CIEINR data model, enabling the creation of
interoperable data structures and facilitating the export of patient
data into Phenopackets. This approach aligns with the goals of
improving diagnosis, treatment, and research for IEI patients, as
detailed in [Genotype-first approach to the diagnosis of primary immunodeficiencies: a Canadian perspective](https://www.sciencedirect.com/science/article/abs/pii/S1521661624001268).

This project integrates with RareLink to export data into Phenopackets,
promoting data sharing and analysis using standardized formats. The
forms used in this project are developed based on the rules found in
[RareLink's documentation for developing REDCap instruments](https://rarelink.readthedocs.io/en/latest/4_user_guide/4_5_develop_redcap_instruments.html).

## Features

* **LinkML Data Model:** Defines the structure of the CIEINR data,
  ensuring data consistency and interoperability.
* **USIDNET Catalogue:** The CIEINR data model is based upon the USIDNET data 
  model. A detailed mapping will follow soon. 
* **RareLink Integration:** Enables the export of CIEINR data into
  Phenopackets.
* **Phenopacket Generation:** Facilitates the creation of standardized
  Phenopackets for patient data.
* **REDCap Instrument Alignment:** The forms are developed using the
  guidelines for Rarelink and REDCap integration.
* **Data Standardization:** Promotes the use of standardized
  terminologies and data formats.

## Getting Started

### Prerequisites

* Python 3.10, 3.11, or 3.12 (not compatible with Python 3.13 due to LinkML dependencies)
* pip
* Git (for cloning the repository with submodules)
* LinkML Toolkit (1.8.0+)

### Installation

1. Clone the repository with submodules:
   ```bash
   git clone https://github.com/your-org/cieinr.git
   cd cieinr
   git submodule update --init --recursive
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
   ```

3. Install the package in development mode:
   ```bash
   pip install -e .
   ```

   This will install CIEINR and its dependencies, including RareLink from the submodule.

### Usage

### CIEINR Data Model

You can find the LinkML definition of the entire **CIEINR-REDCap data model** here:

- [LinkML Schemas](https://github.com/BIH-CEI/cieinr/blob/develop/src/cieinr/v1_0_0/linkml_schemas)

And the corresponding **Python schemas** here:

- [Python Schemas](https://github.com/BIH-CEI/cieinr/blob/develop/src/cieinr/v1_0_0/python_schemas)

All value sets are also defined in these locations.

#### IUIS2024 Classification (MONDO-encoded)

CIEINR implements the complete **IUIS2024 classification** and encodes all disease values using **MONDO**.

You can find the disease definitions in this file:

- [form_1_basic.yaml](https://github.com/BIH-CEI/cieinr/blob/6b596031eb927e9f3e4a69f631a64310ec94ba23/src/cieinr/v1_0_0/linkml_schemas/form_1_basic.yaml)

Or import the enum directly via:

```python
from src.cieinr.v1_0_0.python_schemas.form_1_basic import IUIS2024MONDOEnum
```

> ⚠️ 45 diseases are not yet represented in MONDO. Workshops with ESID, USIDNET, and others are planned to improve MONDO coverage of immunological diseases. Contact us for more info. All other diseases are MONDO-encoded, enabling harmonized Phenopackets for precise downstream analysis.

---

### Installing RareLink

RareLink is included as a **Git submodule** and installed automatically with the package.

To make sure it is set up correctly, run:

```bash
rarelink framework update
rarelink framework status
```

---

### Setup and Export from REDCap

First, configure the REDCap API keys for your local REDCap project:

```bash
rarelink setup keys
```

Check the configuration with:

```bash
rarelink setup view
```

> **Important:** Ensure `.env` and `rarelink_apiconfig.json` are listed in `.gitignore`. These contain sensitive credentials and must remain local and private.

Once data has been captured, download it with:

```bash
rarelink redcap download-records
```

Move and rename the raw REDCap data file to:

```
res/redcap_data.json
```

Then transform the data into the CIEINR-LinkML format:

```bash
python src/cieinr/utils/transform_redcap2linkml.py
```

---

### Phenopacket Export

Once transformation is complete, export the data as Phenopackets using:

```bash
rarelink phenopackets export \
  --input-path cieinr_linkml.json \
  --output-dir res/phenopackets \
  --mappings src/cieinr/v1_0_0/mappings/phenopackets/combined.py
```

> 🔐 **Note:** All data must remain within your local site and secure environment.


## License

This repository and the data model of the  Canadian Inborn Errors of Immunity 
National Registry (CIEINR) is licensed under an [open-source Apache 2.0 license](https://github.com/BIH-CEI/cieinr/develop/LICENSE)

## Acknowledgements

* This project is inspired by the research on inborn errors of
  immunity and the need for standardized data collection. 
* We acknowledge the RareLink project for providing the tools and
  guidelines for Phenopacket generation.
* We acknowledge the paper, [Genotype-first approach to the diagnosis
  of primary immunodeficiencies: a Canadian perspective](https://www.sciencedirect.com/science/article/abs/pii/S1521661624001268),
  for the general information regarding CIEINR.