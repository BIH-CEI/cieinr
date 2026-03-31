# Auto generated from 03_infections_initial_form.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-31T12:45:27
# Schema: infections_initial
#
# id: https://github.com/BIH-CEI/cieinr/src/cieinr/v1_0_0/limkml_schemas/form_3_infections_initial_form.yaml
# description: Initial infections form with infection types, severity, onset dates, causing agents, and patterns for Phenopackets export.
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
HP = CurieNamespace('HP', 'https://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'https://purl.obolibrary.org/obo/MONDO_')
NCBITAXON = CurieNamespace('NCBITAXON', 'https://www.ncbi.nlm.nih.gov/taxonomy')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
SNOMEDCT = CurieNamespace('SNOMEDCT', 'http://snomed.info/sct/')
CIEINR = CurieNamespace('cieinr', 'https://github.com/BIH-CEI/cieinr')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CIEINR


# Types
class UnionDateString(String):
    """ A field that allows both dates and empty strings. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "union_date_string"
    type_model_uri = CIEINR.UnionDateString


class AgeInYears(Integer):
    """ Age in completed years """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "age_in_years"
    type_model_uri = CIEINR.AgeInYears


class AgeInMonths(Integer):
    """ Age in completed months """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "age_in_months"
    type_model_uri = CIEINR.AgeInMonths


class Percent(Float):
    """ A percentage value """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "percent"
    type_model_uri = CIEINR.Percent


class IeiCode(String):
    """ A code for an Inborn Error of Immunity """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "iei_code"
    type_model_uri = CIEINR.IeiCode


class LabValue(Float):
    """ A laboratory measurement value, can be negative in some cases """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "lab_value"
    type_model_uri = CIEINR.LabValue


class PositiveLabValue(Float):
    """ A laboratory measurement value that cannot be negative """
    type_class_uri = XSD["float"]
    type_class_curie = "xsd:float"
    type_name = "positive_lab_value"
    type_model_uri = CIEINR.PositiveLabValue


class NonNegativeInteger(Integer):
    """ An integer value that cannot be negative """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "non_negative_integer"
    type_model_uri = CIEINR.NonNegativeInteger


class TextOrNull(String):
    """ A text field that can be empty or null """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "text_or_null"
    type_model_uri = CIEINR.TextOrNull


class CodedValue(String):
    """ A coded value from a standardized terminology """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "coded_value"
    type_model_uri = CIEINR.CodedValue


class RedcapCheckbox(String):
    """ REDCap checkbox field (contains checked values as comma-separated list) """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "redcap_checkbox"
    type_model_uri = CIEINR.RedcapCheckbox


class RedcapCompletionStatus(String):
    """ REDCap form completion status """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "redcap_completion_status"
    type_model_uri = CIEINR.RedcapCompletionStatus


class BooleanAsInteger(Integer):
    """ Boolean represented as 0 (false) or 1 (true) """
    type_class_uri = XSD["integer"]
    type_class_curie = "xsd:integer"
    type_name = "boolean_as_integer"
    type_model_uri = CIEINR.BooleanAsInteger


# Class references



@dataclass(repr=False)
class InfectionsInitial(YAMLRoot):
    """
    Initial infection information with infection types, severity, and patterns for Phenopackets export.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["InfectionsInitial"]
    class_class_curie: ClassVar[str] = "cieinr:InfectionsInitial"
    class_name: ClassVar[str] = "InfectionsInitial"
    class_model_uri: ClassVar[URIRef] = CIEINR.InfectionsInitial

    infections_initial_form_complete: Union[str, "CompletionStatusEnum"] = None
    type_of_infection: Optional[Union[str, "InfectionTypeEnum"]] = None
    snomedct_61274003: Optional[Union[str, "OpportunisticInfectionEnum"]] = None
    snomedct_21483005: Optional[Union[str, "CNSInfectionEnum"]] = None
    snomedct_81745001: Optional[Union[str, "EyeInfectionEnum"]] = None
    snomedct_385383008: Optional[Union[str, "ENTInfectionEnum"]] = None
    snomedct_127856007: Optional[Union[str, "SkinInfectionEnum"]] = None
    snomedct_110522009: Optional[Union[str, "BoneJointInfectionEnum"]] = None
    snomedct_20139000: Optional[Union[str, "RespiratoryInfectionEnum"]] = None
    snomedct_303699009: Optional[Union[str, "GIInfectionEnum"]] = None
    snomedct_21514008: Optional[Union[str, "GUInfectionEnum"]] = None
    snomedct_31099001: Optional[Union[str, "SystemicInfectionEnum"]] = None
    other_infection_hpo: Optional[Union[str, "HP"]] = None
    other_infection_mondo: Optional[Union[str, "MONDO"]] = None
    infection_severity: Optional[Union[str, "InfectionSeverityEnum"]] = None
    causing_agent: Optional[Union[str, "CausingAgentEnum"]] = None
    causing_agent_viral: Optional[Union[str, "ViralCausingAgentEnum"]] = None
    causing_agent_bacterial: Optional[Union[str, "BacterialCausingAgentEnum"]] = None
    causing_agent_mycotic: Optional[Union[str, "MycoticCausingAgentEnum"]] = None
    causing_organism_other: Optional[str] = None
    infection_temp_pattern: Optional[Union[str, "InfectionTemporalPatternEnum"]] = None
    infection_times_obseverd: Optional[Union[str, "InfectionFrequencyEnum"]] = None
    infection_date: Optional[Union[str, UnionDateString]] = None
    infection_date_2: Optional[Union[str, UnionDateString]] = None
    infection_date_3: Optional[Union[str, UnionDateString]] = None
    infection_date_4: Optional[Union[str, UnionDateString]] = None
    infection_date_5: Optional[Union[str, UnionDateString]] = None
    infection_date_6: Optional[Union[str, UnionDateString]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.infections_initial_form_complete):
            self.MissingRequiredField("infections_initial_form_complete")
        if not isinstance(self.infections_initial_form_complete, CompletionStatusEnum):
            self.infections_initial_form_complete = CompletionStatusEnum(self.infections_initial_form_complete)

        if self.type_of_infection is not None and not isinstance(self.type_of_infection, InfectionTypeEnum):
            self.type_of_infection = InfectionTypeEnum(self.type_of_infection)

        if self.snomedct_61274003 is not None and not isinstance(self.snomedct_61274003, OpportunisticInfectionEnum):
            self.snomedct_61274003 = OpportunisticInfectionEnum(self.snomedct_61274003)

        if self.snomedct_21483005 is not None and not isinstance(self.snomedct_21483005, CNSInfectionEnum):
            self.snomedct_21483005 = CNSInfectionEnum(self.snomedct_21483005)

        if self.snomedct_81745001 is not None and not isinstance(self.snomedct_81745001, EyeInfectionEnum):
            self.snomedct_81745001 = EyeInfectionEnum(self.snomedct_81745001)

        if self.snomedct_385383008 is not None and not isinstance(self.snomedct_385383008, ENTInfectionEnum):
            self.snomedct_385383008 = ENTInfectionEnum(self.snomedct_385383008)

        if self.snomedct_127856007 is not None and not isinstance(self.snomedct_127856007, SkinInfectionEnum):
            self.snomedct_127856007 = SkinInfectionEnum(self.snomedct_127856007)

        if self.snomedct_110522009 is not None and not isinstance(self.snomedct_110522009, BoneJointInfectionEnum):
            self.snomedct_110522009 = BoneJointInfectionEnum(self.snomedct_110522009)

        if self.snomedct_20139000 is not None and not isinstance(self.snomedct_20139000, RespiratoryInfectionEnum):
            self.snomedct_20139000 = RespiratoryInfectionEnum(self.snomedct_20139000)

        if self.snomedct_303699009 is not None and not isinstance(self.snomedct_303699009, GIInfectionEnum):
            self.snomedct_303699009 = GIInfectionEnum(self.snomedct_303699009)

        if self.snomedct_21514008 is not None and not isinstance(self.snomedct_21514008, GUInfectionEnum):
            self.snomedct_21514008 = GUInfectionEnum(self.snomedct_21514008)

        if self.snomedct_31099001 is not None and not isinstance(self.snomedct_31099001, SystemicInfectionEnum):
            self.snomedct_31099001 = SystemicInfectionEnum(self.snomedct_31099001)

        if self.infection_severity is not None and not isinstance(self.infection_severity, InfectionSeverityEnum):
            self.infection_severity = InfectionSeverityEnum(self.infection_severity)

        if self.causing_agent is not None and not isinstance(self.causing_agent, CausingAgentEnum):
            self.causing_agent = CausingAgentEnum(self.causing_agent)

        if self.causing_agent_viral is not None and not isinstance(self.causing_agent_viral, ViralCausingAgentEnum):
            self.causing_agent_viral = ViralCausingAgentEnum(self.causing_agent_viral)

        if self.causing_agent_bacterial is not None and not isinstance(self.causing_agent_bacterial, BacterialCausingAgentEnum):
            self.causing_agent_bacterial = BacterialCausingAgentEnum(self.causing_agent_bacterial)

        if self.causing_agent_mycotic is not None and not isinstance(self.causing_agent_mycotic, MycoticCausingAgentEnum):
            self.causing_agent_mycotic = MycoticCausingAgentEnum(self.causing_agent_mycotic)

        if self.causing_organism_other is not None and not isinstance(self.causing_organism_other, str):
            self.causing_organism_other = str(self.causing_organism_other)

        if self.infection_temp_pattern is not None and not isinstance(self.infection_temp_pattern, InfectionTemporalPatternEnum):
            self.infection_temp_pattern = InfectionTemporalPatternEnum(self.infection_temp_pattern)

        if self.infection_times_obseverd is not None and not isinstance(self.infection_times_obseverd, InfectionFrequencyEnum):
            self.infection_times_obseverd = InfectionFrequencyEnum(self.infection_times_obseverd)

        if self.infection_date is not None and not isinstance(self.infection_date, UnionDateString):
            self.infection_date = UnionDateString(self.infection_date)

        if self.infection_date_2 is not None and not isinstance(self.infection_date_2, UnionDateString):
            self.infection_date_2 = UnionDateString(self.infection_date_2)

        if self.infection_date_3 is not None and not isinstance(self.infection_date_3, UnionDateString):
            self.infection_date_3 = UnionDateString(self.infection_date_3)

        if self.infection_date_4 is not None and not isinstance(self.infection_date_4, UnionDateString):
            self.infection_date_4 = UnionDateString(self.infection_date_4)

        if self.infection_date_5 is not None and not isinstance(self.infection_date_5, UnionDateString):
            self.infection_date_5 = UnionDateString(self.infection_date_5)

        if self.infection_date_6 is not None and not isinstance(self.infection_date_6, UnionDateString):
            self.infection_date_6 = UnionDateString(self.infection_date_6)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CodeSystemsContainer(YAMLRoot):
    """
    A container class for all code systems used in CIEINR.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CIEINR["CodeSystemsContainer"]
    class_class_curie: ClassVar[str] = "cieinr:CodeSystemsContainer"
    class_name: ClassVar[str] = "CodeSystemsContainer"
    class_model_uri: ClassVar[URIRef] = CIEINR.CodeSystemsContainer

    ncbi_taxon: Union[str, "NCBITaxon"] = None
    snomedct: Union[str, "SNOMEDCT"] = None
    mondo: Union[str, "MONDO"] = None
    hpo: Union[str, "HP"] = None
    loinc: Union[str, "LOINC"] = None
    omim: Union[str, "OMIM"] = None
    ncit: Union[str, "NCIT"] = None
    uo: Union[str, "UO"] = None
    hgnc: Union[str, "HGNC"] = None
    hgvs: Union[str, "HGVS"] = None
    ga4gh: Union[str, "GA4GH"] = None
    hl7fhir: Union[str, "HL7FHIR"] = None
    icd11: Union[str, "ICD11"] = None
    icd10cm: Union[str, "ICD10CM"] = None
    bioportal: Union[str, "BIOPORTAL"] = None
    iuis: Union[str, "IUIS"] = None
    maxo: Union[str, "MAXO"] = None

# Enumerations
class InfectionTypeEnum(EnumDefinitionImpl):
    """
    Types of infections
    """
    snomedct_61274003 = PermissibleValue(
        text="snomedct_61274003",
        description="Opportunistic Infection",
        meaning=SNOMEDCT["61274003"])
    snomedct_21483005 = PermissibleValue(
        text="snomedct_21483005",
        description="CNS Infection",
        meaning=SNOMEDCT["21483005"])
    snomedct_81745001 = PermissibleValue(
        text="snomedct_81745001",
        description="Eye Infection",
        meaning=SNOMEDCT["81745001"])
    snomedct_385383008 = PermissibleValue(
        text="snomedct_385383008",
        description="ENT Infection",
        meaning=SNOMEDCT["385383008"])
    snomedct_127856007 = PermissibleValue(
        text="snomedct_127856007",
        description="Skin and Soft Tissue Infection",
        meaning=SNOMEDCT["127856007"])
    snomedct_110522009 = PermissibleValue(
        text="snomedct_110522009",
        description="Bone and Joint Infection",
        meaning=SNOMEDCT["110522009"])
    snomedct_20139000 = PermissibleValue(
        text="snomedct_20139000",
        description="Respiratory Infection",
        meaning=SNOMEDCT["20139000"])
    snomedct_303699009 = PermissibleValue(
        text="snomedct_303699009",
        description="Gastrointestinal Infection",
        meaning=SNOMEDCT["303699009"])
    snomedct_21514008 = PermissibleValue(
        text="snomedct_21514008",
        description="Genitourinary Infections",
        meaning=SNOMEDCT["21514008"])
    snomedct_31099001 = PermissibleValue(
        text="snomedct_31099001",
        description="Systemic Infection",
        meaning=SNOMEDCT["31099001"])

    _defn = EnumDefinition(
        name="InfectionTypeEnum",
        description="Types of infections",
    )

class OpportunisticInfectionEnum(EnumDefinitionImpl):
    """
    Types of opportunistic infections
    """
    mondo_0002026 = PermissibleValue(
        text="mondo_0002026",
        description="Candidiasis",
        meaning=MONDO["0002026"])
    mondo_0005132 = PermissibleValue(
        text="mondo_0005132",
        description="CMV (cytomegalovirus)",
        meaning=MONDO["0005132"])
    mondo_0005724 = PermissibleValue(
        text="mondo_0005724",
        description="Cryptococcosis",
        meaning=MONDO["0005724"])

    _defn = EnumDefinition(
        name="OpportunisticInfectionEnum",
        description="Types of opportunistic infections",
    )

class CNSInfectionEnum(EnumDefinitionImpl):
    """
    Types of CNS infections
    """
    hp_0030049 = PermissibleValue(
        text="hp_0030049",
        description="Brain Abscess",
        meaning=HP["0030049"])
    hp_0002383 = PermissibleValue(
        text="hp_0002383",
        description="Encephalitis",
        meaning=HP["0002383"])
    hp_0001287 = PermissibleValue(
        text="hp_0001287",
        description="Meningitis",
        meaning=HP["0001287"])

    _defn = EnumDefinition(
        name="CNSInfectionEnum",
        description="Types of CNS infections",
    )

class EyeInfectionEnum(EnumDefinitionImpl):
    """
    Types of eye infections
    """
    hp_0000509 = PermissibleValue(
        text="hp_0000509",
        description="Conjunctivitis",
        meaning=HP["0000509"])

    _defn = EnumDefinition(
        name="EyeInfectionEnum",
        description="Types of eye infections",
    )

class ENTInfectionEnum(EnumDefinitionImpl):
    """
    Types of ENT infections
    """
    hp_0000265 = PermissibleValue(
        text="hp_0000265",
        description="Mastoiditis",
        meaning=HP["0000265"])
    hp_0000388 = PermissibleValue(
        text="hp_0000388",
        description="Otitis Media",
        meaning=HP["0000388"])
    hp_0025439 = PermissibleValue(
        text="hp_0025439",
        description="Pharyngitis",
        meaning=HP["0025439"])
    hp_0012384 = PermissibleValue(
        text="hp_0012384",
        description="Rhinitis",
        meaning=HP["0012384"])
    hp_0001731 = PermissibleValue(
        text="hp_0001731",
        description="Sinusitis",
        meaning=HP["0001731"])

    _defn = EnumDefinition(
        name="ENTInfectionEnum",
        description="Types of ENT infections",
    )

class SkinInfectionEnum(EnumDefinitionImpl):
    """
    Types of skin and soft tissue infections
    """
    hp_0100658 = PermissibleValue(
        text="hp_0100658",
        description="Cellulitis",
        meaning=HP["0100658"])
    mondo_0015908 = PermissibleValue(
        text="mondo_0015908",
        description="Fungal Dermatitis",
        meaning=MONDO["0015908"])
    mondo_0043653 = PermissibleValue(
        text="mondo_0043653",
        description="Herpes Labialis (cold sores)",
        meaning=MONDO["0043653"])

    _defn = EnumDefinition(
        name="SkinInfectionEnum",
        description="Types of skin and soft tissue infections",
    )

class BoneJointInfectionEnum(EnumDefinitionImpl):
    """
    Types of bone and joint infections
    """
    hp_0002754 = PermissibleValue(
        text="hp_0002754",
        description="Osteomyelitis",
        meaning=HP["0002754"])
    hp_0003095 = PermissibleValue(
        text="hp_0003095",
        description="Septic Arthritis",
        meaning=HP["0003095"])

    _defn = EnumDefinition(
        name="BoneJointInfectionEnum",
        description="Types of bone and joint infections",
    )

class RespiratoryInfectionEnum(EnumDefinitionImpl):
    """
    Types of respiratory infections
    """
    hp_0012387 = PermissibleValue(
        text="hp_0012387",
        description="Bronchitis, acute",
        meaning=HP["0012387"])
    hp_0004469 = PermissibleValue(
        text="hp_0004469",
        description="Pneumonia",
        meaning=HP["0004469"])

    _defn = EnumDefinition(
        name="RespiratoryInfectionEnum",
        description="Types of respiratory infections",
    )

class GIInfectionEnum(EnumDefinitionImpl):
    """
    Types of gastrointestinal infections
    """
    mondo_0005790 = PermissibleValue(
        text="mondo_0005790",
        description="Hepatitis A",
        meaning=MONDO["0005790"])
    mondo_0005344 = PermissibleValue(
        text="mondo_0005344",
        description="Hepatitis B",
        meaning=MONDO["0005344"])
    mondo_0005231 = PermissibleValue(
        text="mondo_0005231",
        description="Hepatitis C",
        meaning=MONDO["0005231"])
    hp_0002014 = PermissibleValue(
        text="hp_0002014",
        description="Diarrhea",
        meaning=HP["0002014"])

    _defn = EnumDefinition(
        name="GIInfectionEnum",
        description="Types of gastrointestinal infections",
    )

class GUInfectionEnum(EnumDefinitionImpl):
    """
    Types of genitourinary infections
    """
    mondo_0021697 = PermissibleValue(
        text="mondo_0021697",
        description="Chlamydia",
        meaning=MONDO["0021697"])
    hp_0100577 = PermissibleValue(
        text="hp_0100577",
        description="Cystitis",
        meaning=HP["0100577"])
    mondo_0005770 = PermissibleValue(
        text="mondo_0005770",
        description="Genital Herpes",
        meaning=MONDO["0005770"])
    mondo_0004277 = PermissibleValue(
        text="mondo_0004277",
        description="Gonorrhea",
        meaning=MONDO["0004277"])

    _defn = EnumDefinition(
        name="GUInfectionEnum",
        description="Types of genitourinary infections",
    )

class SystemicInfectionEnum(EnumDefinitionImpl):
    """
    Types of systemic infections
    """
    hp_0031864 = PermissibleValue(
        text="hp_0031864",
        description="Bacteremia",
        meaning=HP["0031864"])
    mondo_0024619 = PermissibleValue(
        text="mondo_0024619",
        description="Central Venous Line Infections",
        meaning=MONDO["0024619"])
    mondo_0005132 = PermissibleValue(
        text="mondo_0005132",
        description="CMV",
        meaning=MONDO["0005132"])

    _defn = EnumDefinition(
        name="SystemicInfectionEnum",
        description="Types of systemic infections",
    )

class InfectionSeverityEnum(EnumDefinitionImpl):
    """
    Severity levels of infections
    """
    hp_0012825 = PermissibleValue(
        text="hp_0012825",
        description="Mild (localized or oral intervention required)",
        meaning=HP["0012825"])
    hp_0012826 = PermissibleValue(
        text="hp_0012826",
        description="Moderate (IV medication required)",
        meaning=HP["0012826"])
    hp_0012828 = PermissibleValue(
        text="hp_0012828",
        description="Severe (hospitalization required or prolonged)",
        meaning=HP["0012828"])

    _defn = EnumDefinition(
        name="InfectionSeverityEnum",
        description="Severity levels of infections",
    )

class InfectionTemporalPatternEnum(EnumDefinitionImpl):
    """
    Temporal patterns of infections
    """
    hp_0011009 = PermissibleValue(
        text="hp_0011009",
        description="Acute (< 2 weeks, rapid progression)",
        meaning=HP["0011009"])
    hp_0011011 = PermissibleValue(
        text="hp_0011011",
        description="Subacute (2 weeks to 3 months, slow increase)",
        meaning=HP["0011011"])
    hp_0011010 = PermissibleValue(
        text="hp_0011010",
        description="Chronic (> 3 months)",
        meaning=HP["0011010"])
    hp_0031796 = PermissibleValue(
        text="hp_0031796",
        description="Recurrent",
        meaning=HP["0031796"])

    _defn = EnumDefinition(
        name="InfectionTemporalPatternEnum",
        description="Temporal patterns of infections",
    )

class InfectionFrequencyEnum(EnumDefinitionImpl):
    """
    Frequency of infection
    """
    ncit_c64576 = PermissibleValue(
        text="ncit_c64576",
        description="1",
        meaning=NCIT["C64576"])
    ncit_c65134 = PermissibleValue(
        text="ncit_c65134",
        description="2",
        meaning=NCIT["C65134"])
    ncit_c156502 = PermissibleValue(
        text="ncit_c156502",
        description="3",
        meaning=NCIT["C156502"])
    ncit_c200364 = PermissibleValue(
        text="ncit_c200364",
        description="4",
        meaning=NCIT["C200364"])
    ncit_c66836 = PermissibleValue(
        text="ncit_c66836",
        description="5",
        meaning=NCIT["C66836"])

    _defn = EnumDefinition(
        name="InfectionFrequencyEnum",
        description="Frequency of infection",
    )

class CausingAgentEnum(EnumDefinitionImpl):
    """
    Classes of causing agents
    """
    ncbitaxon_10239 = PermissibleValue(
        text="ncbitaxon_10239",
        description="Viral",
        meaning=NCBITAXON["10239"])
    ncbitaxon_2 = PermissibleValue(
        text="ncbitaxon_2",
        description="Bacterial",
        meaning=CIEINR["Bacterial"])
    ncbitaxon_4751 = PermissibleValue(
        text="ncbitaxon_4751",
        description="Mycotic",
        meaning=NCBITAXON["4751"])
    other = PermissibleValue(
        text="other",
        description="Other",
        meaning=CIEINR["Other"])
    unknown = PermissibleValue(
        text="unknown",
        description="unknown",
        meaning=CIEINR["unknown"])

    _defn = EnumDefinition(
        name="CausingAgentEnum",
        description="Classes of causing agents",
    )

class ViralCausingAgentEnum(EnumDefinitionImpl):
    """
    Classes of viral causing agents
    """
    ncbitaxon_10508 = PermissibleValue(
        text="ncbitaxon_10508",
        description="Adenovirus",
        meaning=NCBITAXON["10508"])
    ncbitaxon_2697049 = PermissibleValue(
        text="ncbitaxon_2697049",
        description="Adenovirus",
        meaning=NCBITAXON["2697049"])
    ncbitaxon_10358 = PermissibleValue(
        text="ncbitaxon_10358",
        description="COVID 19",
        meaning=NCBITAXON["10358"])
    ebv_virus = PermissibleValue(
        text="ebv_virus",
        description="EBV virus",
        meaning=CIEINR["EBV_VIRUS"])
    ncbitaxon_12059 = PermissibleValue(
        text="ncbitaxon_12059",
        description="Entero/rhinovirus",
        meaning=NCBITAXON["12059"])
    ncbitaxon_10407 = PermissibleValue(
        text="ncbitaxon_10407",
        description="Hepatitis B virus",
        meaning=NCBITAXON["10407"])
    ncbitaxon_12092 = PermissibleValue(
        text="ncbitaxon_12092",
        description="Hepatitis A virus",
        meaning=NCBITAXON["12092"])
    ncbitaxon_10294 = PermissibleValue(
        text="ncbitaxon_10294",
        description="Herpes Simplex virus",
        meaning=NCBITAXON["10294"])
    ncbitaxon_11320 = PermissibleValue(
        text="ncbitaxon_11320",
        description="Influenza A virus",
        meaning=NCBITAXON["11320"])
    ncbitaxon_11520 = PermissibleValue(
        text="ncbitaxon_11520",
        description="Influenza B virus",
        meaning=NCBITAXON["11520"])
    ncbitaxon_142786 = PermissibleValue(
        text="ncbitaxon_142786",
        description="Norovirus",
        meaning=NCBITAXON["142786"])
    ncbitaxon_12814 = PermissibleValue(
        text="ncbitaxon_12814",
        description="Respiratory syncytial virus",
        meaning=NCBITAXON["12814"])
    ncbitaxon_10912 = PermissibleValue(
        text="ncbitaxon_10912",
        description="Rotavirus",
        meaning=NCBITAXON["10912"])
    ncbitaxon_10335 = PermissibleValue(
        text="ncbitaxon_10335",
        description="Varicella Zoster",
        meaning=NCBITAXON["10335"])
    causing_agent_viral_other = PermissibleValue(
        text="causing_agent_viral_other",
        description="Other",
        meaning=CIEINR["causing_agent_viral_other"])

    _defn = EnumDefinition(
        name="ViralCausingAgentEnum",
        description="Classes of viral causing agents",
    )

class BacterialCausingAgentEnum(EnumDefinitionImpl):
    """
    Classes of bacterial causing agents
    """
    ncbitaxon_31979 = PermissibleValue(
        text="ncbitaxon_31979",
        description="Clostridium diff",
        meaning=NCBITAXON["31979"])
    ncbitaxon_91347 = PermissibleValue(
        text="ncbitaxon_91347",
        description="Enterobacter",
        meaning=NCBITAXON["91347"])
    ncbitaxon_81852 = PermissibleValue(
        text="ncbitaxon_81852",
        description="Enterococcus (including E. coli)",
        meaning=NCBITAXON["81852"])
    ncbitaxon_724 = PermissibleValue(
        text="ncbitaxon_724",
        description="Haemophilus",
        meaning=NCBITAXON["724"])
    snomedct_75032006 = PermissibleValue(
        text="snomedct_75032006",
        description="Klebsiella",
        meaning=SNOMEDCT["75032006"])
    ncbitaxon_33958 = PermissibleValue(
        text="ncbitaxon_33958",
        description="Lactobacillaceae",
        meaning=NCBITAXON["33958"])
    ncbitaxon_445 = PermissibleValue(
        text="ncbitaxon_445",
        description="Legionella",
        meaning=NCBITAXON["445"])
    ncbitaxon_186820 = PermissibleValue(
        text="ncbitaxon_186820",
        description="Listeriaceae",
        meaning=NCBITAXON["186820"])
    ncbitaxon_2093 = PermissibleValue(
        text="ncbitaxon_2093",
        description="Mycoplasma",
        meaning=NCBITAXON["2093"])
    ncbitaxon_482 = PermissibleValue(
        text="ncbitaxon_482",
        description="Neisseria meningitis",
        meaning=NCBITAXON["482"])
    ncbitaxon_90964 = PermissibleValue(
        text="ncbitaxon_90964",
        description="Staphylococcus",
        meaning=NCBITAXON["90964"])
    ncbitaxon_1300 = PermissibleValue(
        text="ncbitaxon_1300",
        description="Streptococcus",
        meaning=NCBITAXON["1300"])
    causing_agent_bacterial_other = PermissibleValue(
        text="causing_agent_bacterial_other",
        description="Other",
        meaning=CIEINR["causing_agent_bacterial_other"])

    _defn = EnumDefinition(
        name="BacterialCausingAgentEnum",
        description="Classes of bacterial causing agents",
    )

class MycoticCausingAgentEnum(EnumDefinitionImpl):
    """
    Classes of mycotic causing agents
    """
    ncbitaxon_5052 = PermissibleValue(
        text="ncbitaxon_5052",
        description="Aspergillus",
        meaning=NCBITAXON["5052"])
    ncbitaxon_5475 = PermissibleValue(
        text="ncbitaxon_5475",
        description="Candida",
        meaning=NCBITAXON["5475"])
    ncbitaxon_470132 = PermissibleValue(
        text="ncbitaxon_470132",
        description="Catenulostroma chromoblastomycosum",
        meaning=NCBITAXON["470132"])
    ncbitaxon_3027 = PermissibleValue(
        text="ncbitaxon_3027",
        description="Cryptophyceae",
        meaning=NCBITAXON["3027"])
    ncbitaxon_2231446 = PermissibleValue(
        text="ncbitaxon_2231446",
        description="Dermatophyllum",
        meaning=NCBITAXON["2231446"])
    ncbitaxon_5036 = PermissibleValue(
        text="ncbitaxon_5036",
        description="Histoplasma",
        meaning=NCBITAXON["5036"])
    ncbitaxon_370836 = PermissibleValue(
        text="ncbitaxon_370836",
        description="Pityriasis",
        meaning=NCBITAXON["370836"])
    ncbitaxon_4753 = PermissibleValue(
        text="ncbitaxon_4753",
        description="Pneumocystis",
        meaning=NCBITAXON["4753"])
    ncbitaxon_184471 = PermissibleValue(
        text="ncbitaxon_184471",
        description="Sporotrichum",
        meaning=NCBITAXON["184471"])
    ncbitaxon_41013 = PermissibleValue(
        text="ncbitaxon_41013",
        description="Tinea (including tinea corporis)",
        meaning=NCBITAXON["41013"])
    causing_agent_mycotic_other = PermissibleValue(
        text="causing_agent_mycotic_other",
        description="Other",
        meaning=CIEINR["causing_agent_mycotic_other"])

    _defn = EnumDefinition(
        name="MycoticCausingAgentEnum",
        description="Classes of mycotic causing agents",
    )

class CompletionStatusEnum(EnumDefinitionImpl):
    """
    Enumeration for form completion status
    """
    _defn = EnumDefinition(
        name="CompletionStatusEnum",
        description="""Enumeration for form completion status""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
            PermissibleValue(
                text="0",
                description="Incomplete"))
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="Unverified"))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="Complete"))

class NCBITaxon(EnumDefinitionImpl):
    """
    NCBI organismal classification
    """
    _defn = EnumDefinition(
        name="NCBITaxon",
        description="NCBI organismal classification",
        code_set=URIRef(str(NCBITAXON)),
        code_set_version="2025_04_10",
    )

class SNOMEDCT(EnumDefinitionImpl):
    """
    SNOMED CT
    """
    _defn = EnumDefinition(
        name="SNOMEDCT",
        description="SNOMED CT",
        code_set_version="2025AB",
    )

class MONDO(EnumDefinitionImpl):
    """
    Monarch Disease Ontology
    """
    _defn = EnumDefinition(
        name="MONDO",
        description="Monarch Disease Ontology",
        code_set_version="2026-03-03",
    )

class HP(EnumDefinitionImpl):
    """
    Human Phenotype Ontology
    """
    _defn = EnumDefinition(
        name="HP",
        description="Human Phenotype Ontology",
        code_set_version="2026-02-16",
    )

class LOINC(EnumDefinitionImpl):
    """
    Logical Observation Identifiers Names and Codes
    """
    _defn = EnumDefinition(
        name="LOINC",
        description="Logical Observation Identifiers Names and Codes",
        code_set_version="281",
    )

class OMIM(EnumDefinitionImpl):
    """
    Online Mendelian Inheritance
    """
    _defn = EnumDefinition(
        name="OMIM",
        description="Online Mendelian Inheritance",
        code_set_version="OMIM2024_08_09",
    )

class NCIT(EnumDefinitionImpl):
    """
    NCI Thesaurus OBO Edition
    """
    _defn = EnumDefinition(
        name="NCIT",
        description="NCI Thesaurus OBO Edition",
        code_set_version="26.02d",
    )

class UO(EnumDefinitionImpl):
    """
    Units of Measurement Ontology
    """
    _defn = EnumDefinition(
        name="UO",
        description="Units of Measurement Ontology",
        code_set_version="2026-01-16",
    )

class HGNC(EnumDefinitionImpl):
    """
    HUGO Gene Nomenclature Committee
    """
    _defn = EnumDefinition(
        name="HGNC",
        description="HUGO Gene Nomenclature Committee",
        code_set_version="2024-08-23",
    )

class HGVS(EnumDefinitionImpl):
    """
    Human Genome Variation Society
    """
    _defn = EnumDefinition(
        name="HGVS",
        description="Human Genome Variation Society",
        code_set_version="21.0.0",
    )

class GA4GH(EnumDefinitionImpl):
    """
    Global Alliance for Genomics and Health
    """
    _defn = EnumDefinition(
        name="GA4GH",
        description="Global Alliance for Genomics and Health",
        code_set_version="v2.0",
    )

class HL7FHIR(EnumDefinitionImpl):
    """
    Health Level 7 Fast Healthcare Interoperability Resources
    """
    _defn = EnumDefinition(
        name="HL7FHIR",
        description="Health Level 7 Fast Healthcare Interoperability Resources",
        code_set_version="v4.0.1",
    )

class ICD11(EnumDefinitionImpl):
    """
    International Classification of Diseases, Eleventh Revision
    """
    _defn = EnumDefinition(
        name="ICD11",
        description="International Classification of Diseases, Eleventh Revision",
        code_set_version="2025AB",
    )

class ICD10CM(EnumDefinitionImpl):
    """
    International Classification of Diseases, Tenth Revision, Clinical Modification
    """
    _defn = EnumDefinition(
        name="ICD10CM",
        description="International Classification of Diseases, Tenth Revision, Clinical Modification",
        code_set_version="CD10CM_2025",
    )

class SO(EnumDefinitionImpl):
    """
    Sequence types and features ontology
    """
    _defn = EnumDefinition(
        name="SO",
        description="Sequence types and features ontology",
        code_set_version="2.6",
    )

class GENO(EnumDefinitionImpl):
    """
    GENO - The Genotype Ontology
    """
    _defn = EnumDefinition(
        name="GENO",
        description="GENO - The Genotype Ontology",
        code_set_version="2026-02-02",
    )

class ISO3166(EnumDefinitionImpl):
    """
    ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes
    """
    _defn = EnumDefinition(
        name="ISO3166",
        description="ISO 3166-1:2020(en) alpha-2 and alpha-3 country codes",
        code_set_version="2020(en)",
    )

class ICF(EnumDefinitionImpl):
    """
    International Classification of Functioning, Disability and Health
    """
    _defn = EnumDefinition(
        name="ICF",
        description="International Classification of Functioning, Disability and Health",
        code_set_version="1.0.2",
    )

class MAXO(EnumDefinitionImpl):
    """
    Medical Action Ontology
    """
    _defn = EnumDefinition(
        name="MAXO",
        description="Medical Action Ontology",
        code_set_version="2025-04-24",
    )

class BIOPORTAL(EnumDefinitionImpl):
    """
    BioPortal ontology repository
    """
    _defn = EnumDefinition(
        name="BIOPORTAL",
        description="BioPortal ontology repository",
        code_set_version="2024-09-01",
    )

class IUIS(EnumDefinitionImpl):
    """
    International Union of Immunological Societies Classification
    """
    _defn = EnumDefinition(
        name="IUIS",
        description="International Union of Immunological Societies Classification",
        code_set_version="2024",
    )

# Slots
class slots:
    pass

slots.type_of_infection = Slot(uri=CIEINR.type_of_infection, name="type_of_infection", curie=CIEINR.curie('type_of_infection'),
                   model_uri=CIEINR.type_of_infection, domain=None, range=Optional[Union[str, "InfectionTypeEnum"]])

slots.snomedct_61274003 = Slot(uri=CIEINR.snomedct_61274003, name="snomedct_61274003", curie=CIEINR.curie('snomedct_61274003'),
                   model_uri=CIEINR.snomedct_61274003, domain=None, range=Optional[Union[str, "OpportunisticInfectionEnum"]])

slots.snomedct_21483005 = Slot(uri=CIEINR.snomedct_21483005, name="snomedct_21483005", curie=CIEINR.curie('snomedct_21483005'),
                   model_uri=CIEINR.snomedct_21483005, domain=None, range=Optional[Union[str, "CNSInfectionEnum"]])

slots.snomedct_81745001 = Slot(uri=CIEINR.snomedct_81745001, name="snomedct_81745001", curie=CIEINR.curie('snomedct_81745001'),
                   model_uri=CIEINR.snomedct_81745001, domain=None, range=Optional[Union[str, "EyeInfectionEnum"]])

slots.snomedct_385383008 = Slot(uri=CIEINR.snomedct_385383008, name="snomedct_385383008", curie=CIEINR.curie('snomedct_385383008'),
                   model_uri=CIEINR.snomedct_385383008, domain=None, range=Optional[Union[str, "ENTInfectionEnum"]])

slots.snomedct_127856007 = Slot(uri=CIEINR.snomedct_127856007, name="snomedct_127856007", curie=CIEINR.curie('snomedct_127856007'),
                   model_uri=CIEINR.snomedct_127856007, domain=None, range=Optional[Union[str, "SkinInfectionEnum"]])

slots.snomedct_110522009 = Slot(uri=CIEINR.snomedct_110522009, name="snomedct_110522009", curie=CIEINR.curie('snomedct_110522009'),
                   model_uri=CIEINR.snomedct_110522009, domain=None, range=Optional[Union[str, "BoneJointInfectionEnum"]])

slots.snomedct_20139000 = Slot(uri=CIEINR.snomedct_20139000, name="snomedct_20139000", curie=CIEINR.curie('snomedct_20139000'),
                   model_uri=CIEINR.snomedct_20139000, domain=None, range=Optional[Union[str, "RespiratoryInfectionEnum"]])

slots.snomedct_303699009 = Slot(uri=CIEINR.snomedct_303699009, name="snomedct_303699009", curie=CIEINR.curie('snomedct_303699009'),
                   model_uri=CIEINR.snomedct_303699009, domain=None, range=Optional[Union[str, "GIInfectionEnum"]])

slots.snomedct_21514008 = Slot(uri=CIEINR.snomedct_21514008, name="snomedct_21514008", curie=CIEINR.curie('snomedct_21514008'),
                   model_uri=CIEINR.snomedct_21514008, domain=None, range=Optional[Union[str, "GUInfectionEnum"]])

slots.snomedct_31099001 = Slot(uri=CIEINR.snomedct_31099001, name="snomedct_31099001", curie=CIEINR.curie('snomedct_31099001'),
                   model_uri=CIEINR.snomedct_31099001, domain=None, range=Optional[Union[str, "SystemicInfectionEnum"]])

slots.other_infection_hpo = Slot(uri=CIEINR.other_infection_hpo, name="other_infection_hpo", curie=CIEINR.curie('other_infection_hpo'),
                   model_uri=CIEINR.other_infection_hpo, domain=None, range=Optional[Union[str, "HP"]])

slots.other_infection_mondo = Slot(uri=CIEINR.other_infection_mondo, name="other_infection_mondo", curie=CIEINR.curie('other_infection_mondo'),
                   model_uri=CIEINR.other_infection_mondo, domain=None, range=Optional[Union[str, "MONDO"]])

slots.infection_severity = Slot(uri=CIEINR.infection_severity, name="infection_severity", curie=CIEINR.curie('infection_severity'),
                   model_uri=CIEINR.infection_severity, domain=None, range=Optional[Union[str, "InfectionSeverityEnum"]])

slots.infection_temp_pattern = Slot(uri=CIEINR.infection_temp_pattern, name="infection_temp_pattern", curie=CIEINR.curie('infection_temp_pattern'),
                   model_uri=CIEINR.infection_temp_pattern, domain=None, range=Optional[Union[str, "InfectionTemporalPatternEnum"]])

slots.causing_agent = Slot(uri=CIEINR.causing_agent, name="causing_agent", curie=CIEINR.curie('causing_agent'),
                   model_uri=CIEINR.causing_agent, domain=None, range=Optional[Union[str, "CausingAgentEnum"]])

slots.causing_agent_viral = Slot(uri=CIEINR.causing_agent_viral, name="causing_agent_viral", curie=CIEINR.curie('causing_agent_viral'),
                   model_uri=CIEINR.causing_agent_viral, domain=None, range=Optional[Union[str, "ViralCausingAgentEnum"]])

slots.causing_agent_bacterial = Slot(uri=CIEINR.causing_agent_bacterial, name="causing_agent_bacterial", curie=CIEINR.curie('causing_agent_bacterial'),
                   model_uri=CIEINR.causing_agent_bacterial, domain=None, range=Optional[Union[str, "BacterialCausingAgentEnum"]])

slots.causing_agent_mycotic = Slot(uri=CIEINR.causing_agent_mycotic, name="causing_agent_mycotic", curie=CIEINR.curie('causing_agent_mycotic'),
                   model_uri=CIEINR.causing_agent_mycotic, domain=None, range=Optional[Union[str, "MycoticCausingAgentEnum"]])

slots.causing_organism_other = Slot(uri=CIEINR.causing_organism_other, name="causing_organism_other", curie=CIEINR.curie('causing_organism_other'),
                   model_uri=CIEINR.causing_organism_other, domain=None, range=Optional[str])

slots.infection_times_obseverd = Slot(uri=CIEINR.infection_times_obseverd, name="infection_times_obseverd", curie=CIEINR.curie('infection_times_obseverd'),
                   model_uri=CIEINR.infection_times_obseverd, domain=None, range=Optional[Union[str, "InfectionFrequencyEnum"]])

slots.infection_date = Slot(uri=CIEINR.infection_date, name="infection_date", curie=CIEINR.curie('infection_date'),
                   model_uri=CIEINR.infection_date, domain=None, range=Optional[Union[str, UnionDateString]])

slots.infection_date_2 = Slot(uri=CIEINR.infection_date_2, name="infection_date_2", curie=CIEINR.curie('infection_date_2'),
                   model_uri=CIEINR.infection_date_2, domain=None, range=Optional[Union[str, UnionDateString]])

slots.infection_date_3 = Slot(uri=CIEINR.infection_date_3, name="infection_date_3", curie=CIEINR.curie('infection_date_3'),
                   model_uri=CIEINR.infection_date_3, domain=None, range=Optional[Union[str, UnionDateString]])

slots.infection_date_4 = Slot(uri=CIEINR.infection_date_4, name="infection_date_4", curie=CIEINR.curie('infection_date_4'),
                   model_uri=CIEINR.infection_date_4, domain=None, range=Optional[Union[str, UnionDateString]])

slots.infection_date_5 = Slot(uri=CIEINR.infection_date_5, name="infection_date_5", curie=CIEINR.curie('infection_date_5'),
                   model_uri=CIEINR.infection_date_5, domain=None, range=Optional[Union[str, UnionDateString]])

slots.infection_date_6 = Slot(uri=CIEINR.infection_date_6, name="infection_date_6", curie=CIEINR.curie('infection_date_6'),
                   model_uri=CIEINR.infection_date_6, domain=None, range=Optional[Union[str, UnionDateString]])

slots.infections_initial_form_complete = Slot(uri=CIEINR.infections_initial_form_complete, name="infections_initial_form_complete", curie=CIEINR.curie('infections_initial_form_complete'),
                   model_uri=CIEINR.infections_initial_form_complete, domain=None, range=Union[str, "CompletionStatusEnum"])

slots.codeSystemsContainer__ncbi_taxon = Slot(uri=CIEINR.ncbi_taxon, name="codeSystemsContainer__ncbi_taxon", curie=CIEINR.curie('ncbi_taxon'),
                   model_uri=CIEINR.codeSystemsContainer__ncbi_taxon, domain=None, range=Union[str, "NCBITaxon"])

slots.codeSystemsContainer__snomedct = Slot(uri=CIEINR.snomedct, name="codeSystemsContainer__snomedct", curie=CIEINR.curie('snomedct'),
                   model_uri=CIEINR.codeSystemsContainer__snomedct, domain=None, range=Union[str, "SNOMEDCT"])

slots.codeSystemsContainer__mondo = Slot(uri=CIEINR.mondo, name="codeSystemsContainer__mondo", curie=CIEINR.curie('mondo'),
                   model_uri=CIEINR.codeSystemsContainer__mondo, domain=None, range=Union[str, "MONDO"])

slots.codeSystemsContainer__hpo = Slot(uri=CIEINR.hpo, name="codeSystemsContainer__hpo", curie=CIEINR.curie('hpo'),
                   model_uri=CIEINR.codeSystemsContainer__hpo, domain=None, range=Union[str, "HP"])

slots.codeSystemsContainer__loinc = Slot(uri=CIEINR.loinc, name="codeSystemsContainer__loinc", curie=CIEINR.curie('loinc'),
                   model_uri=CIEINR.codeSystemsContainer__loinc, domain=None, range=Union[str, "LOINC"])

slots.codeSystemsContainer__omim = Slot(uri=CIEINR.omim, name="codeSystemsContainer__omim", curie=CIEINR.curie('omim'),
                   model_uri=CIEINR.codeSystemsContainer__omim, domain=None, range=Union[str, "OMIM"])

slots.codeSystemsContainer__ncit = Slot(uri=CIEINR.ncit, name="codeSystemsContainer__ncit", curie=CIEINR.curie('ncit'),
                   model_uri=CIEINR.codeSystemsContainer__ncit, domain=None, range=Union[str, "NCIT"])

slots.codeSystemsContainer__uo = Slot(uri=CIEINR.uo, name="codeSystemsContainer__uo", curie=CIEINR.curie('uo'),
                   model_uri=CIEINR.codeSystemsContainer__uo, domain=None, range=Union[str, "UO"])

slots.codeSystemsContainer__hgnc = Slot(uri=CIEINR.hgnc, name="codeSystemsContainer__hgnc", curie=CIEINR.curie('hgnc'),
                   model_uri=CIEINR.codeSystemsContainer__hgnc, domain=None, range=Union[str, "HGNC"])

slots.codeSystemsContainer__hgvs = Slot(uri=CIEINR.hgvs, name="codeSystemsContainer__hgvs", curie=CIEINR.curie('hgvs'),
                   model_uri=CIEINR.codeSystemsContainer__hgvs, domain=None, range=Union[str, "HGVS"])

slots.codeSystemsContainer__ga4gh = Slot(uri=CIEINR.ga4gh, name="codeSystemsContainer__ga4gh", curie=CIEINR.curie('ga4gh'),
                   model_uri=CIEINR.codeSystemsContainer__ga4gh, domain=None, range=Union[str, "GA4GH"])

slots.codeSystemsContainer__hl7fhir = Slot(uri=CIEINR.hl7fhir, name="codeSystemsContainer__hl7fhir", curie=CIEINR.curie('hl7fhir'),
                   model_uri=CIEINR.codeSystemsContainer__hl7fhir, domain=None, range=Union[str, "HL7FHIR"])

slots.codeSystemsContainer__icd11 = Slot(uri=CIEINR.icd11, name="codeSystemsContainer__icd11", curie=CIEINR.curie('icd11'),
                   model_uri=CIEINR.codeSystemsContainer__icd11, domain=None, range=Union[str, "ICD11"])

slots.codeSystemsContainer__icd10cm = Slot(uri=CIEINR.icd10cm, name="codeSystemsContainer__icd10cm", curie=CIEINR.curie('icd10cm'),
                   model_uri=CIEINR.codeSystemsContainer__icd10cm, domain=None, range=Union[str, "ICD10CM"])

slots.codeSystemsContainer__bioportal = Slot(uri=CIEINR.bioportal, name="codeSystemsContainer__bioportal", curie=CIEINR.curie('bioportal'),
                   model_uri=CIEINR.codeSystemsContainer__bioportal, domain=None, range=Union[str, "BIOPORTAL"])

slots.codeSystemsContainer__iuis = Slot(uri=CIEINR.iuis, name="codeSystemsContainer__iuis", curie=CIEINR.curie('iuis'),
                   model_uri=CIEINR.codeSystemsContainer__iuis, domain=None, range=Union[str, "IUIS"])

slots.codeSystemsContainer__maxo = Slot(uri=CIEINR.maxo, name="codeSystemsContainer__maxo", curie=CIEINR.curie('maxo'),
                   model_uri=CIEINR.codeSystemsContainer__maxo, domain=None, range=Union[str, "MAXO"])

