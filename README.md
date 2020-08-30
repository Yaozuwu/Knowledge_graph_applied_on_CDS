# Knowledge_graph_applied_on_CDS

| Metanode    | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Compound    | Approved small molecule compounds with documented chemical structures. From [DrugBank](https://www.drugbank.ca/). |
| Anatomy     | Anatomical structures, excluding structures that are known not to be found in humans. From [Uberon](http://uberon.github.io/). |
| Disease     | Complex diseases, selected to be distinct and specific enough to be clinically relevant yet general enough to be well annotated. From [Disease Ontology](http://disease-ontology.org/). |
| Symptom     | Signs and Symptoms (i.e. clinical abnormalities that can indicate a medical condition). From the [MeSH ontology](https://www.nlm.nih.gov/mesh/meshhome.html). |
| Side Effect | Adverse drug reactions. From [SIDER](http://sideeffects.embl.de/)/[UMLS](https://www.nlm.nih.gov/research/umls/). |
| Atc         |                                                              |





| Entity type | Drugbank | GNBR | Hetionet | Total Entities |
| ----------- | -------- | ---- | -------- | -------------- |
| Anatomy     |          |      | 398      |                |
| Atc         | 4,048    |      |          |                |
| Compound    |          |      |          | 1,0458         |
| Disease     |          |      |          | 4,022          |
| Side Effect |          |      | 5,701    | 5,701          |
| Symptom     |          |      | 415      |                |







| Entity-type pair        | Drugbank | GNBR   | Hetionet | Total interactions |
| ----------------------- | -------- | ------ | -------- | ------------------ |
| (Atc, Compound)         | 15,750   |        |          |                    |
| (Compound, Disease)     | 4,968    | 77,782 | 1,145    | 83,895             |
| (Disease, Symptom)      |          |        | 3,357    |                    |
| (Anatomy, Disease)      |          |        | 3,602    |                    |
| (Disease, Disease)      |          |        | 543      |                    |
| (Compound, Side Effect) |          |        | 138,944  |                    |

