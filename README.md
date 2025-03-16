# Canadian Inborn Errors of Immunity National Registry (CIEINR) Data Model

[![Python 3.10-3.12](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LinkML](https://img.shields.io/badge/LinkML-1.8.0+-green.svg)](https://linkml.io/)

This repository houses the LinkML representation of the data model for
the Canadian Inborn Errors of Immunity National Registry (CIEINR). This
project facilitates the export of patient data into Phenopackets,
leveraging RareLink's functionalities.

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
immunity (IEI) across Canada. This repository provides the LinkML
representation of the CIEINR data model, enabling the creation of
interoperable data structures and facilitating the export of patient
data into Phenopackets. This approach aligns with the goals of
improving diagnosis, treatment, and research for IEI patients, as
detailed in [Genotype-first approach to the diagnosis of primary
immunodeficiencies: a Canadian perspective](https://www.sciencedirect.
com/science/article/abs/pii/S1521661624001268).

This project integrates with RareLink to export data into Phenopackets,
promoting data sharing and analysis using standardized formats. The
forms used in this project are developed based on the rules found in
[RareLink's documentation for developing REDCap instruments](https://
rarelink.readthedocs.io/en/latest/4_user_guide/4_5_develop_redcap_
instruments.html).

## Features

* **LinkML Data Model:** Defines the structure of the CIEINR data,
  ensuring data consistency and interoperability.
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

## Usage

### Importing from RareLink

RareLink is included as a submodule and installed automatically with the package. You can import RareLink components directly in your code:

```python
# Import utilities from RareLink
from rarelink.utils.processor import DataProcessor
from rarelink.utils.processing.codes import process_redcap_code

# Import phenopackets components
from rarelink.phenopackets import create_phenopacket, write_phenopackets
from rarelink.phenopackets.mappings import map_diseases, map_individual
```

### Generating Phenopackets

This project primarily focuses on the LinkML representation of the
CIEINR data model. You can use the LinkML schema to:

* Generate data validation tools.
* Create data transformation scripts.
* Export data into various formats, including Phenopackets using
  RareLink.

Example of generating a phenopacket:

```python
from rarelink.phenopackets import create_phenopacket, write_phenopackets
from rarelink.utils.processor import DataProcessor
from cieinr.v1_0_0.mappings.linkml_to_phenopackets import (
    INDIVIDUAL_BLOCK, DISEASE_BLOCK, PHENOTYPIC_FEATURES_BLOCK
)

# Process a record with RareLink
def transform_to_phenopacket(record):
    # Initialize processors with CIEINR-specific mapping configurations
    individual_processor = DataProcessor(mapping_config=INDIVIDUAL_BLOCK)
    disease_processor = DataProcessor(mapping_config=DISEASE_BLOCK)
    
    # Create phenopacket
    phenopacket = create_phenopacket(record, "CIEINR")
    return phenopacket

# More detailed examples can be found in the Rarelink documentation:
# https://rarelink.readthedocs.io/en/latest/4_user_guide/4_3_phenopackets.html
```

## License

Specify the license under which your project is distributed. (e.g., MIT)

## Acknowledgements

* This project is inspired by the research on inborn errors of
  immunity and the need for standardized data collection. 
* We acknowledge the RareLink project for providing the tools and
  guidelines for Phenopacket generation.
* We acknowledge the paper, [Genotype-first approach to the diagnosis
  of primary immunodeficiencies: a Canadian perspective](https://
  www.sciencedirect.com/science/article/abs/pii/S1521661624001268),
  for the general information regarding CIEINR.