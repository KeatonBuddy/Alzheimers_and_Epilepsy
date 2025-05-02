# Alzheimer's and Epilepsy: A Genetic Relationship
## Project Overview
This project investigates the genetic relationship between Alzheimer’s disease and epilepsy, aiming to identify genes whose expressions overlap significantly in these conditions. Recent epidemiological studies suggest increased epilepsy risk in Alzheimer’s patients, hinting at common genetic factors. By uncovering genes with similar expression patterns in both diseases, this project seeks to facilitate the development of treatments effective for both conditions.

*This work was conducted to fulfill the MDSC 397 course requirement at the University of Calgary*

## Objectives
- Identify genetic expression similarities between Alzheimer's and epilepsy.

- Determine the statistical significance of these genetic overlaps.

- Explore potential shared treatment options based on identified genetic pathways.

## Methodology
The analysis pipeline involved three key stages:

- Data Curation and Preprocessing

- Gene expression data for Alzheimer's, epilepsy, and healthy controls were collected from the Allen Brain Atlas database.

- Raw data underwent preprocessing steps to normalize and standardize expression levels across groups.

## Gene Expression Analysis

- Python scripts (findmean.py, findMeanAndStd.py) were implemented to compute the mean and standard deviation for gene expressions across Alzheimer's, epilepsy, and control samples.

- The statistical significance of expression differences was tested using Python scripts (Compare.py, TESTfindMeanAndStd.py) through a t-score analysis, calculating degrees of freedom and evaluating p-values.

## Identification of Common Genetic Targets

- Genes exhibiting statistically similar expression patterns in both Alzheimer’s and epilepsy, distinct from controls, were identified.

- Databases SMPDB and DrugBank were consulted to map these genes to potential drug treatments that affect their gene products.

## Repository Contents
Data Analysis Scripts:

- findmean.py: Calculates mean gene expressions for Alzheimer's and control datasets.

- findMeanAndStd.py: Computes both mean and standard deviation for each gene expression data set.

- TESTfindMeanAndStd.py: An optimized and comprehensive script for calculating statistics concurrently across multiple datasets.

- Compare.py: Performs statistical comparisons (t-score and degrees of freedom) between Alzheimer’s and control gene expression datasets.

## Documentation:

- Proposal.pdf: Detailed project proposal outlining background, objectives, and pipeline.

## Analysis Outputs:

- CSV files containing computed statistical measures and comparison results (e.g., ComparedFile.csv), indicating genes with significant expression similarities.

## Key Findings
- Identified candidate genes that share similar expression profiles in Alzheimer's and epilepsy, potentially contributing to the epidemiological association between these conditions.

- Proposed shared therapeutic targets, offering a basis for future drug repurposing studies.

## Future Directions
- Further validation of identified genes in clinical and experimental settings.

- Exploration of gene expression impacts on clinical outcomes and drug response.

## Technologies and Tools
- Languages: Python, R

- Libraries/Packages: Pandas, CSV, Statistics, Multiprocessing

- Databases: Allen Brain Atlas, SMPDB, DrugBank, Genome Home Reference

- Statistical Tools: Limma package (R/Bioconductor)
