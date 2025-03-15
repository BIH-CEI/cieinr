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

Instructions on how to set up and run your project locally.

### Prerequisites

* Python 3.10, 3.11, or 3.12 (not compatible with Python 3.13 due to LinkML dependencies)
* pip
* RareLink (if you need to generate phenopackets)
* LinkML Toolkit (1.8.0+)

### Installation

Step-by-step instructions on how to install and set up your project.

To install your own code run `pip install -e .` in a terminal.

## Usage

This project primarily focuses on the LinkML representation of the
CIEINR data model. You can use the LinkML schema to:

* Generate data validation tools.
* Create data transformation scripts.
* Export data into various formats, including Phenopackets using
  RareLink.
* Follow the instructions found in the Rarelink documentation to
  export phenopackets. [Rarelink phenopackets documentation](https://
  rarelink.readthedocs.io/en/latest/4_user_guide/4_3_phenopackets.html)

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