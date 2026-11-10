# AOR: Automated Ontology Resource
 
## Objective
 
The objective of this project is to automatically generate an ontology from data of different types (unstructured text, semi-structured files such as JSON/XML, and structured tables), with minimal human intervention.
 
## Overview
 
AOR (Automated Ontology Resource) is an end-to-end pipeline that ingests heterogeneous data, extracts concepts, hierarchies and relations, and produces a reusable ontology resource in a standardized format (RDF/OWL). It combines NLP, machine learning and LLMs, and includes a human validation step to ensure the quality and consistency of the result.
 
## Features
 
- **Multi-format ingestion**: PDF, web pages, CSV, JSON, XML, databases
- **Concept extraction**: term candidates, synonym grouping, clustering
- **Hierarchy detection**: "is-a" (taxonomy) relations
- **Relation extraction**: domain-specific relations using NLP and LLMs
- **Ontology export**: RDF/OWL (Turtle, RDF/XML)
- **Visualization**: interactive concept graph
- **Human validation**: web interface to accept or reject proposed relations
- **Evaluation**: precision/recall against a reference ontology