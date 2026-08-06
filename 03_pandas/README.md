# Stage 3: pandas

This stage builds on Python and NumPy by adding labeled rows and columns. The examples progress from table fundamentals to a reusable corpus-annotation cleaning pipeline. No external dataset is required.

## Prerequisite

Complete `../02_numpy/README.md`. In particular, be comfortable with arrays, Boolean masks, vectorized operations, aggregations, and reproducible random sampling.

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

## Learning pattern

Both notebooks use small, self-contained tables. Read the explanation, run the example, change one value or condition, and complete the embedded practice before moving on.

## What you should be able to do afterward

- create, inspect, select, filter, and sort `Series` and `DataFrame` objects;
- clean missing, duplicated, textual, categorical, and date values;
- summarize and reshape data with grouping, cross-tabulation, and pivot tables;
- combine tables safely with validated joins;
- build a reusable cleaning function and run final quality checks.

## Next stage

Continue to `../04_matplotlib/README.md` to turn cleaned tables and numerical summaries into interpretable figures.
