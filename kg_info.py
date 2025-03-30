NODE_INFO = [
{
  "identity": -102,
  "labels": [
    "disease"
  ],
  "properties": {
    "name": "disease",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-102"
}
, 
{
  "identity": -108,
  "labels": [
    "exposure"
  ],
  "properties": {
    "name": "exposure",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-108"
}
, 
{
  "identity": -101,
  "labels": [
    "anatomy"
  ],
  "properties": {
    "name": "anatomy",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-101"
}
, 
{
  "identity": -105,
  "labels": [
    "biological_process"
  ],
  "properties": {
    "name": "biological_process",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-105"
}
, 
{
  "identity": -103,
  "labels": [
    "effect__phenotype"
  ],
  "properties": {
    "name": "effect__phenotype",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-103"
}
, 
{
  "identity": -109,
  "labels": [
    "pathway"
  ],
  "properties": {
    "name": "pathway",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-109"
}
, 
{
  "identity": -100,
  "labels": [
    "gene__protein"
  ],
  "properties": {
    "name": "gene__protein",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-100"
}
, 
{
  "identity": -107,
  "labels": [
    "cellular_component"
  ],
  "properties": {
    "name": "cellular_component",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-107"
}
, 
{
  "identity": -104,
  "labels": [
    "drug"
  ],
  "properties": {
    "name": "drug",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-104"
}
, 
{
  "identity": -106,
  "labels": [
    "molecular_function"
  ],
  "properties": {
    "name": "molecular_function",
    "indexes": [],
    "constraints": []
  },
  "elementId": "-106"
}
]

RELATIONSHIP_INFO = [
{
  "identity": -102,
  "start": -100,
  "end": -106,
  "type": "molfunc_protein",
  "properties": {
    "name": "molfunc_protein"
  },
  "elementId": "-102",
  "startNodeElementId": "-100",
  "endNodeElementId": "-106"
}
, 
{
  "identity": -106,
  "start": -100,
  "end": -105,
  "type": "bioprocess_protein",
  "properties": {
    "name": "bioprocess_protein"
  },
  "elementId": "-106",
  "startNodeElementId": "-100",
  "endNodeElementId": "-105"
}
, 
{
  "identity": -125,
  "start": -102,
  "end": -103,
  "type": "disease_phenotype_positive",
  "properties": {
    "name": "disease_phenotype_positive"
  },
  "elementId": "-125",
  "startNodeElementId": "-102",
  "endNodeElementId": "-103"
}
, 
{
  "identity": -126,
  "start": -103,
  "end": -102,
  "type": "disease_phenotype_positive",
  "properties": {
    "name": "disease_phenotype_positive"
  },
  "elementId": "-126",
  "startNodeElementId": "-103",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -124,
  "start": -102,
  "end": -102,
  "type": "disease_phenotype_positive",
  "properties": {
    "name": "disease_phenotype_positive"
  },
  "elementId": "-124",
  "startNodeElementId": "-102",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -127,
  "start": -103,
  "end": -103,
  "type": "disease_phenotype_positive",
  "properties": {
    "name": "disease_phenotype_positive"
  },
  "elementId": "-127",
  "startNodeElementId": "-103",
  "endNodeElementId": "-103"
}
, 
{
  "identity": -130,
  "start": -102,
  "end": -102,
  "type": "disease_disease",
  "properties": {
    "name": "disease_disease"
  },
  "elementId": "-130",
  "startNodeElementId": "-102",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -116,
  "start": -106,
  "end": -106,
  "type": "molfunc_molfunc",
  "properties": {
    "name": "molfunc_molfunc"
  },
  "elementId": "-116",
  "startNodeElementId": "-106",
  "endNodeElementId": "-106"
}
, 
{
  "identity": -115,
  "start": -108,
  "end": -107,
  "type": "exposure_cellcomp",
  "properties": {
    "name": "exposure_cellcomp"
  },
  "elementId": "-115",
  "startNodeElementId": "-108",
  "endNodeElementId": "-107"
}
, 
{
  "identity": -103,
  "start": -104,
  "end": -103,
  "type": "drug_effect",
  "properties": {
    "name": "drug_effect"
  },
  "elementId": "-103",
  "startNodeElementId": "-104",
  "endNodeElementId": "-103"
}
, 
{
  "identity": -112,
  "start": -108,
  "end": -105,
  "type": "exposure_bioprocess",
  "properties": {
    "name": "exposure_bioprocess"
  },
  "elementId": "-112",
  "startNodeElementId": "-108",
  "endNodeElementId": "-105"
}
, 
{
  "identity": -129,
  "start": -103,
  "end": -103,
  "type": "phenotype_phenotype",
  "properties": {
    "name": "phenotype_phenotype"
  },
  "elementId": "-129",
  "startNodeElementId": "-103",
  "endNodeElementId": "-103"
}
, 
{
  "identity": -105,
  "start": -101,
  "end": -101,
  "type": "anatomy_anatomy",
  "properties": {
    "name": "anatomy_anatomy"
  },
  "elementId": "-105",
  "startNodeElementId": "-101",
  "endNodeElementId": "-101"
}
, 
{
  "identity": -123,
  "start": -104,
  "end": -100,
  "type": "drug_protein",
  "properties": {
    "name": "drug_protein"
  },
  "elementId": "-123",
  "startNodeElementId": "-104",
  "endNodeElementId": "-100"
}
, 
{
  "identity": -108,
  "start": -100,
  "end": -109,
  "type": "pathway_protein",
  "properties": {
    "name": "pathway_protein"
  },
  "elementId": "-108",
  "startNodeElementId": "-100",
  "endNodeElementId": "-109"
}
, 
{
  "identity": -120,
  "start": -104,
  "end": -102,
  "type": "contraindication",
  "properties": {
    "name": "contraindication"
  },
  "elementId": "-120",
  "startNodeElementId": "-104",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -110,
  "start": -108,
  "end": -100,
  "type": "exposure_protein",
  "properties": {
    "name": "exposure_protein"
  },
  "elementId": "-110",
  "startNodeElementId": "-108",
  "endNodeElementId": "-100"
}
, 
{
  "identity": -128,
  "start": -102,
  "end": -103,
  "type": "disease_phenotype_negative",
  "properties": {
    "name": "disease_phenotype_negative"
  },
  "elementId": "-128",
  "startNodeElementId": "-102",
  "endNodeElementId": "-103"
}
, 
{
  "identity": -101,
  "start": -100,
  "end": -101,
  "type": "anatomy_protein_present",
  "properties": {
    "name": "anatomy_protein_present"
  },
  "elementId": "-101",
  "startNodeElementId": "-100",
  "endNodeElementId": "-101"
}
, 
{
  "identity": -113,
  "start": -109,
  "end": -109,
  "type": "pathway_pathway",
  "properties": {
    "name": "pathway_pathway"
  },
  "elementId": "-113",
  "startNodeElementId": "-109",
  "endNodeElementId": "-109"
}
, 
{
  "identity": -131,
  "start": -100,
  "end": -102,
  "type": "disease_protein",
  "properties": {
    "name": "disease_protein"
  },
  "elementId": "-131",
  "startNodeElementId": "-100",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -100,
  "start": -100,
  "end": -100,
  "type": "protein_protein",
  "properties": {
    "name": "protein_protein"
  },
  "elementId": "-100",
  "startNodeElementId": "-100",
  "endNodeElementId": "-100"
}
, 
{
  "identity": -109,
  "start": -108,
  "end": -102,
  "type": "exposure_disease",
  "properties": {
    "name": "exposure_disease"
  },
  "elementId": "-109",
  "startNodeElementId": "-108",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -117,
  "start": -107,
  "end": -107,
  "type": "cellcomp_cellcomp",
  "properties": {
    "name": "cellcomp_cellcomp"
  },
  "elementId": "-117",
  "startNodeElementId": "-107",
  "endNodeElementId": "-107"
}
, 
{
  "identity": -132,
  "start": -100,
  "end": -103,
  "type": "phenotype_protein",
  "properties": {
    "name": "phenotype_protein"
  },
  "elementId": "-132",
  "startNodeElementId": "-100",
  "endNodeElementId": "-103"
}
, 
{
  "identity": -122,
  "start": -104,
  "end": -102,
  "type": "off-label use",
  "properties": {
    "name": "off-label use"
  },
  "elementId": "-122",
  "startNodeElementId": "-104",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -119,
  "start": -104,
  "end": -104,
  "type": "drug_drug",
  "properties": {
    "name": "drug_drug"
  },
  "elementId": "-119",
  "startNodeElementId": "-104",
  "endNodeElementId": "-104"
}
, 
{
  "identity": -104,
  "start": -105,
  "end": -105,
  "type": "bioprocess_bioprocess",
  "properties": {
    "name": "bioprocess_bioprocess"
  },
  "elementId": "-104",
  "startNodeElementId": "-105",
  "endNodeElementId": "-105"
}
, 
{
  "identity": -121,
  "start": -104,
  "end": -102,
  "type": "indication",
  "properties": {
    "name": "indication"
  },
  "elementId": "-121",
  "startNodeElementId": "-104",
  "endNodeElementId": "-102"
}
, 
{
  "identity": -111,
  "start": -108,
  "end": -108,
  "type": "exposure_exposure",
  "properties": {
    "name": "exposure_exposure"
  },
  "elementId": "-111",
  "startNodeElementId": "-108",
  "endNodeElementId": "-108"
}
, 
{
  "identity": -107,
  "start": -100,
  "end": -107,
  "type": "cellcomp_protein",
  "properties": {
    "name": "cellcomp_protein"
  },
  "elementId": "-107",
  "startNodeElementId": "-100",
  "endNodeElementId": "-107"
}
, 
{
  "identity": -118,
  "start": -100,
  "end": -101,
  "type": "anatomy_protein_absent",
  "properties": {
    "name": "anatomy_protein_absent"
  },
  "elementId": "-118",
  "startNodeElementId": "-100",
  "endNodeElementId": "-101"
}
, 
{
  "identity": -114,
  "start": -108,
  "end": -106,
  "type": "exposure_molfunc",
  "properties": {
    "name": "exposure_molfunc"
  },
  "elementId": "-114",
  "startNodeElementId": "-108",
  "endNodeElementId": "-106"
}
]

# relationship_types = [r["type"] for r in RELATIONSHIP_INFO]
# print(relationship_types)

RELATIONSHIP_TYPES = ['molfunc_protein', 'bioprocess_protein', 'disease_phenotype_positive', 'disease_phenotype_positive', 'disease_phenotype_positive', 'disease_phenotype_positive', 'disease_disease', 'molfunc_molfunc', 'exposure_cellcomp', 'drug_effect', 'exposure_bioprocess', 'phenotype_phenotype', 'anatomy_anatomy', 'drug_protein', 'pathway_protein', 'contraindication', 'exposure_protein', 'disease_phenotype_negative', 'anatomy_protein_present', 'pathway_pathway', 'disease_protein', 'protein_protein', 'exposure_disease', 'cellcomp_cellcomp', 'phenotype_protein', 'off-label use', 'drug_drug', 'bioprocess_bioprocess', 'indication', 'exposure_exposure', 'cellcomp_protein', 'anatomy_protein_absent', 'exposure_molfunc']