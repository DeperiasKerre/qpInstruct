## Mining the Heterostructural Design and the Optoelectronic Characterustics of Quantum Cascade Lasers
### Brief Introduction to the Problem

A quantum cascade laser(qcl) is a semiconductor consisting of nanometric stack of different semiconductor materials. The stacks are called heterostructures.The interaction between the different layers of materials gives the stack its opto-electronic characteristics i.e. its radiation emission behavior according to the electric current injected into the structure. The quantum cascade laser is a promising technology for industrial deployment owing to its application potential in the various domains.

Quantum cascade lasers are complex heterostructures but in general, weakly structured post growth. This implies that most of the properties of the laser are defined by its growth sheet, i.e. the description of the different stack layers which include their thickness, the nature of the material, the order, among others. The extraction of these properties therefore plays a vital role in deciphering the general complex heterostructure of the stacks which in turn informs the general structure of the lasers.

### Proposed Approach
The aim is to develop a knowledge graph for exploring the qcl physical parameters and the corresponding opto-electronic effects. The qcl parameters of interest are **physical parameters(the qcl design /stacking properties and thickness)**,and the **optoelectronic characteristics(Temperature,Power and the lasing frequency)**.
This could be exploited to run analyze the different qcl Designs and their corresponding performance by interacting with the graph through queries. Most of the develped knowledge graphs in academic literarure only capture the paper related information such as the author name, publication dates etc. The bigger challenges id to generate Scientific knowlege graphs that also contain an explicit represenattion of knowledge represented in the research publications[[1]](https://oro.open.ac.uk/61767/1/DL4KG_2019_paper_3%20%281%29.pdf). There are several attempts to solving this probelm, but to the best of our knowledge, the exploreation of the qcl parameters remains unexperimented. 

From the review of similar works [[2]](https://arxiv.org/pdf/1807.08484),[[3]](https://hal.archives-ouvertes.fr/hal-02404153/file/ClaimsKG_A_knowledge_graph_of_annotated_claims.pdf), the construction of a knowledge graph requires a consistent ontology capturing  the information to be visualized in form of triples. There is no existing ontology on qcl parameters and therefore the development of the knowledge graph could follow the follwoing steps:

* A text mining pipeline to extract the qcl parameters from the scientific articles (as seen from the sample developed ontology, it may not be possible to represent the data in the garph at concept level before mining it). The ontology can be visualized in neo4j by downloading the turtle file and fetching it using the neosemantics in neo4j as follows: open the neo4j web browser and type: call n10s.rdf.preview.fetch('https://raw.githubusercontent.com/jbarrasa/datasets/master/rdfstar/beatles-hs.ttl',"Turtle-star"). Remember to change the path to refer to the path to your disk. e.g "file:///D:......."

* Organizing the mined properties into a dataset with all the information (authors, publication dates, reference lsit and the qcl propreties).

* Define the schema structure in rdf* using turtle syntax. The proposed enity classes are 2 i.e a paper(which has a name, label,url as the attributes) and qcl parameter class. The qcl parameter may have subclasses i.e physical parameter(to capture the qclthickness and the stacking property) opto-electronics parameter (to capture frequency, temperature and the power). Two major realtions are also proposed i.e cites(to indicate the references) and mentions(to capture the qcl parameter mentioned by a paper). 
### Next Step
After exploring on a simple omtology using rdf and turtle(under ontologies folder), the next step is to now explore a text mining pipeline to extract the properties(it could be important to baer in mind that the qcl parameters are domain specific terms). This could be important in representing information at concept level in the graph.
