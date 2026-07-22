# Pandas

This section of **AI Engineering School** introduces Pandas through small, practical, self-contained examples. The notebooks do not require external datasets.

## Learning order

1. **01_pandas_fundamentals.ipynb**
   - Series and DataFrames
   - inspecting datasets
   - selecting rows and columns
   - `.loc[]` and `.iloc[]`
   - filtering and sorting
   - category counts and cross-tabulations
   - calculated columns
   - basic CSV loading
   - a small corpus-data exercise

2. **02_pandas_data_cleaning_and_analysis.ipynb**
   - renaming, adding, and removing columns
   - missing values
   - text cleaning
   - duplicate records
   - data-type and date conversion
   - conditional columns and mappings
   - `groupby()` and aggregation
   - pivot tables and cross-tabulations
   - `merge()` and `concat()`
   - basic plotting
   - exporting data
   - a reusable cleaning pipeline
   - final data-quality checks

## Suggested repository structure

```text
ai-engineering-school/
└── pandas/
    ├── README.md
    ├── requirements.txt
    ├── 01_pandas_fundamentals.ipynb
    └── 02_pandas_data_cleaning_and_analysis.ipynb
```

## Installation

```bash
pip install -r requirements.txt
```

Or install the libraries directly:

```bash
pip install pandas numpy matplotlib jupyter
```

## Running the notebooks

From the repository directory:

```bash
jupyter notebook
```

You can also open the notebooks in VS Code, JupyterLab, Google Colab, or Kaggle.

## Design notes

- Examples are intentionally small enough to understand visually.
- Operations are explained before they are used.
- The second notebook uses an NLP annotation table to connect Pandas with data preparation for AI and computational linguistics.
- Notebook outputs are cleared to keep the GitHub repository lightweight. Run the cells in order to reproduce them.
Pandas

This section of AI Engineering School introduces Pandas through small, practical, self-contained examples. The notebooks do not require external datasets.

Learning order

01_pandas_fundamentals.ipynb

Series and DataFrames

inspecting datasets

selecting rows and columns

.loc[] and .iloc[]

filtering and sorting

category counts and cross-tabulations

calculated columns

basic CSV loading

a small corpus-data exercise

02_pandas_data_cleaning_and_analysis.ipynb

renaming, adding, and removing columns

missing values

text cleaning

duplicate records

data-type and date conversion

conditional columns and mappings

groupby() and aggregation

pivot tables and cross-tabulations

merge() and concat()

basic plotting

exporting data

a reusable cleaning pipeline

final data-quality checks

Suggested repository structure

ai-engineering-school/
└── pandas/
    ├── README.md
    ├── requirements.txt
    ├── 01_pandas_fundamentals.ipynb
    └── 02_pandas_data_cleaning_and_analysis.ipynb

Installation

pip install -r requirements.txt

Or install the libraries directly:

pip install pandas numpy matplotlib jupyter

Running the notebooks

From the repository directory:

jupyter notebook

You can also open the notebooks in VS Code, JupyterLab, Google Colab, or Kaggle.

Design notes

Examples are intentionally small enough to understand visually.

Operations are explained before they are used.

The second notebook uses an NLP annotation table to connect Pandas with data preparation for AI and computational linguistics.

Notebook outputs are cleared to keep the GitHub repository lightweight. Run the cells in order to reproduce them.
