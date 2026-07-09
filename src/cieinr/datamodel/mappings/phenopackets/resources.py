# src/cieinr/datamodel/mappings/phenopackets/resources.py
"""
Code systems container for CIEINR Phenopacket metadata.

This must be a Python @dataclass so that rarelink's MetadataMapper can call
``dataclasses.fields()`` on it. Each field holds a CodeSystem instance whose
attributes (name, url, version, prefix, iri_prefix) are read by
``_filter_fields_by_prefixes`` in rarelink.

Field names MUST match the keys in rarelink's ``_FIELD_TO_PREFIXES`` dict
(metadata_mapper.py) so prefix-based filtering works correctly.
Versions are aligned with the cieinr_code_systems LinkML schema.
"""
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class CodeSystem:
    """A single ontology / terminology resource."""
    name: str
    prefix: str
    version: str
    url: str
    iri_prefix: str


@dataclass
class CodeSystemsContainer:
    """
    Container for all code systems used in CIEINR.

    Field names correspond to the keys expected by rarelink's
    ``_FIELD_TO_PREFIXES`` mapping so that the MetadataMapper can
    filter resources by the CURIE prefixes actually used in a
    Phenopacket.
    """

    # --- Fields matching rarelink _FIELD_TO_PREFIXES keys ---

    hpo: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Human Phenotype Ontology",
        prefix="HP",
        version="2026-02-16",
        url="https://www.human-phenotype-ontology.org",
        iri_prefix="http://purl.obolibrary.org/obo/HP_",
    ))

    mondo: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Monarch Disease Ontology",
        prefix="MONDO",
        version="2026-03-03",
        url="https://purl.obolibrary.org/obo/MONDO/",
        iri_prefix="http://purl.obolibrary.org/obo/MONDO_",
    ))

    SNOMEDCT: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="SNOMED CT",
        prefix="SNOMEDCT",
        version="2025AB",
        url="http://snomed.info/sct",
        iri_prefix="http://snomed.info/id/",
    ))

    loinc: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Logical Observation Identifiers Names and Codes",
        prefix="LOINC",
        version="281",
        url="http://loinc.org",
        iri_prefix="http://loinc.org/rdf/",
    ))

    omim: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Online Mendelian Inheritance in Man",
        prefix="OMIM",
        version="OMIM2024_08_09",
        url="https://omim.org/",
        iri_prefix="https://www.omim.org/entry/",
    ))

    ncit: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="NCI Thesaurus OBO Edition",
        prefix="NCIT",
        version="26.02d",
        url="http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl",
        iri_prefix="http://purl.obolibrary.org/obo/NCIT_",
    ))

    uo: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Units of Measurement Ontology",
        prefix="UO",
        version="2026-01-16",
        url="https://www.ontobee.org/ontology/UO",
        iri_prefix="http://purl.obolibrary.org/obo/UO_",
    ))

    hgnc: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="HUGO Gene Nomenclature Committee",
        prefix="HGNC",
        version="2024-08-23",
        url="https://www.genenames.org/",
        iri_prefix="https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/",
    ))

    hgvs: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Human Genome Variation Society",
        prefix="HGVS",
        version="21.0.0",
        url="http://varnomen.hgvs.org/",
        iri_prefix="https://varnomen.hgvs.org/recommendations/variant/",
    ))

    ga4gh: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Global Alliance for Genomics and Health",
        prefix="GA4GH",
        version="v2.0",
        url="https://www.ga4gh.org/",
        iri_prefix="https://www.ga4gh.org/",
    ))

    hl7fhir: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Health Level 7 Fast Healthcare Interoperability Resources",
        prefix="HL7FHIR",
        version="v4.0.1",
        url="https://www.hl7.org/fhir",
        iri_prefix="https://www.hl7.org/fhir/",
    ))

    ncbi_taxon: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="NCBI Organismal Classification",
        prefix="NCBITaxon",
        version="2025_04_10",
        url="https://www.ncbi.nlm.nih.gov/taxonomy",
        iri_prefix="http://purl.obolibrary.org/obo/NCBITaxon_",
    ))

    icd11: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="International Classification of Diseases, Eleventh Revision",
        prefix="ICD11",
        version="2025AB",
        url="https://icd.who.int/en",
        iri_prefix="https://icd.who.int/browse11/l-m/en#/",
    ))

    icd10cm: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="International Classification of Diseases, Tenth Revision, Clinical Modification",
        prefix="ICD10CM",
        version="CD10CM_2025",
        url="https://icd10cmtool.cdc.gov/",
        iri_prefix="https://icd10cmtool.cdc.gov/",
    ))

    so: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Sequence Types and Features Ontology",
        prefix="SO",
        version="2.6",
        url="https://www.sequenceontology.org/",
        iri_prefix="http://purl.obolibrary.org/obo/SO_",
    ))

    geno: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="GENO - The Genotype Ontology",
        prefix="GENO",
        version="2026-02-02",
        url="https://www.genoontology.org/",
        iri_prefix="http://purl.obolibrary.org/obo/GENO_",
    ))

    iso3166: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="ISO 3166-1:2020(en) Country Codes",
        prefix="ISO3166",
        version="2020(en)",
        url="https://www.iso.org/iso-3166-country-codes.html",
        iri_prefix="https://www.iso.org/iso-3166-country-codes.html/",
    ))

    icf: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="International Classification of Functioning, Disability and Health",
        prefix="ICF",
        version="1.0.2",
        url="https://www.who.int/classifications/icf/en/",
        iri_prefix="https://www.who.int/classifications/icf/en/",
    ))

    maxo: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Medical Action Ontology",
        prefix="MAXO",
        version="2025-04-24",
        url="https://purl.obolibrary.org/obo/maxo.owl",
        iri_prefix="http://purl.obolibrary.org/obo/MAXO_",
    ))

    # --- CIEINR-specific code systems (not in base rarelink) ---
    vo: Optional[CodeSystem] = field(default_factory=lambda: CodeSystem(
        name="Vaccine Ontology",
        prefix="VO",
        version="2024-09-12",
        url="https://purl.obolibrary.org/obo/vo.owl",
        iri_prefix="http://purl.obolibrary.org/obo/VO_",
    ))


CIEINR_CODE_SYSTEMS = CodeSystemsContainer()