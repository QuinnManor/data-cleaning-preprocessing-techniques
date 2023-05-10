# Data Cleaning & Preprocessing Techniques

This project is a simple walk-through of various data cleaning and preprocessing techniques to consider before doing data analysis.

## Why

Raw data often contains errors, missing values, inconsistencies, and other issues that can negatively impact the quality and reliability of any downstream analyses. By cleaning up, and preprocessing data, one can ensure that the data they are working with is accurate, complete, and in a format that is appropriate for the intended analysis or modeling task. This can lead to more reliable and accurate results, as well as more efficient use of time and resources.

> **Note**: Data cleaning and preprocessing is an iterative process as new issues can be uncovered during analysis or modeling.

## What this IS NOT!

Data cleaning and preprocessing is not a way for you to introduce your own bias. This can happen unintentionally, but the techniques used should be conducted carefully to avoid overemphasizing or underemphasizing aspects of your data.

For example, if a dataset contains missing values, one common approach to address this is to impute the missing values. However, if the missing values are not random, but instead systematically related to other variables in the dataset, then the imputed values may introduce bias into the dataset.

### Prerequisites

- python
- jupyter notebook

### Getting Started

1. `git clone git@github.com:QuinnManor/data-cleaning-preprocessing-techniques.git`
2. `cd data-cleaning-preprocessing-techniques`
3. `jupyter notebook`

## Project Organization

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for analysis.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention: `1 - data-cleaning.ipynb`.
    │
    ├── .gitignore         <- Specifies which files to ignore within the repository.

---
