![CI](https://github.com/fair-data-collective/generic-dataset-metadata-template/workflows/excel2rdf/badge.svg) ![CI](https://github.com/fair-data-collective/generic-dataset-metadata-template/workflows/cedar-artifacts-fetch/badge.svg) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
# Generic Dataset Metadata Template

This project's generic dataset metadata template has been created to satisfy several concrete customer applications:

- the need for a concrete model for delivering metadata to DeIC and DTU organizations
- delivering data set metadata for existing projects in the wind energy domain
- preparing metadata descriptions for use in GOFAIR M4M workshops that deal with metadata
- Research Data Alliance activities supporting data set metadata definition (e.g., the Engineering IG)
- COVID-19 Training workshops organized by GO FAIR in support of ZonMV

The template has the following target capabilities:

- compatibility with a well-known generic metadata modeling and collection system (CEDAR)
- evaluation of and support for GO FAIR FAIR Data Points (FDPs)
- support for RDF production that can be presented (with translation) as nanopublications
- satisfaction of FAIR principles and metadata evaluators
- secure generation of DOI

The template description in the [Excel Sheet](./template-description.xlsx) is intended to provide sufficient detail that it can be used to create a [CEDAR Template](https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2Fc33e855c-4d25-457b-aa97-19b7093493b8),
which in turn can be filled out easily by the dataset creator or contributor.
The template description in the [Excel Sheet](./template-description.xlsx) could also be adopted for other metadata systems.

It should be noted that many FAIR principles and FAIR Data Point ([FDP](https://www.go-fair.org/how-to-go-fair/fair-data-point/)) specifications can not be satisfied by the data creator/contributor,
but must be addressed by the data aggregator and distributor.
These differences will be highlighted as we fill out the details of the template specification.

# Resources
- [CEDAR OpenView representation of the template](https://openview.metadatacenter.org/templates/https:%2F%2Frepo.metadatacenter.org%2Ftemplates%2F17cb90a2-05d0-4b1d-9f4a-6ee3bf9c362b) showing structure of the generic metadata template.
- [Example of the template instance](https://openview.metadatacenter.org/template-instances/https:%2F%2Frepo.metadatacenter.org%2Ftemplate-instances%2F33b76e0c-b09d-4742-9b2d-70aaaa408345) that has been configured for wind energy community by adding [community specific controlled vocabularies for field **subject**](http://bioportal.bioontology.org/ontologies/WETAXTOPICS)
- [Folder](./cedar/assets) containing [CEDAR](https://cedar.metadatacenter.org/) assets, specifically metadata elements, fields and templates provided as [JSON-LD](https://json-ld.org/) files.
- [Slides](./template-presentation.pdf) presenting the generic data metadata template
- [Excel Sheet](./template-description.xlsx) containing details about the metadata fields and elements
- [Excel sheet](./ontology/dataset-voc.xlsx) for building SKOS-based controlled terminologies and RDF/OWL properties for the metadata template.
