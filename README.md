# Knowledge_graph_applied_on_CDS

## Clinical decision support systems

Clinical decision support systems (CDSS) aim to provide clinicians or patients with computer-generated clinical knowledge and patient-related information that can be intelligently filtered or presented at appropriate times, to enhance patient care.

## Purpose:

Our objective is a system that can extract and represent these knowledge contained in EMRs to support three CDS tasks: 

- Determining a patient’s most likely diagnosis given a list of symptoms
- Deciding on the most effective treatment plan for a patient with a known condition
- Determining if a particular test is indicated for a given situation

with the given condition of one patient.





## Knowledge graph

### Introduction:



![Knowledge_Graph_Structure](D:\code\Knowledge_graph_applied_on_CDS\Knowledge_Graph_Structure.jpg)



### Description of entity:

| Metanode    | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Compound    | Approved small molecule compounds with documented chemical structures. From [DrugBank](https://www.drugbank.ca/). |
| Anatomy     | Anatomical structures, excluding structures that are known not to be found in humans. From [Uberon](http://uberon.github.io/). |
| Disease     | Complex diseases, selected to be distinct and specific enough to be clinically relevant yet general enough to be well annotated. From [Disease Ontology](http://disease-ontology.org/). |
| Symptom     | Signs and Symptoms (i.e. clinical abnormalities that can indicate a medical condition). From the [MeSH ontology](https://www.nlm.nih.gov/mesh/meshhome.html). |
| Side Effect | Adverse drug reactions. From [SIDER](http://sideeffects.embl.de/)/[UMLS](https://www.nlm.nih.gov/research/umls/). |
| Atc         |                                                              |
| Treatment   |                                                              |
| Test        |                                                              |
| Test result |                                                              |

| Entity\Attriubte |      |      |
| ---------------- | ---- | ---- |
| Side-effect      |      |      |
| Act              |      |      |
| Compound         |      |      |
| Symptom          |      |      |
| Disease          |      |      |
| Anatomy          |      |      |
| Patient          |      |      |
| Test             |      |      |
| Test Result      |      |      |
| Treatment        |      |      |





## Statistics of knowledge graph

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

