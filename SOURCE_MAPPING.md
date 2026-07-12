# How the uploaded course files were used

This repository is based on the uploaded introduction PDF file and six Python notebooks.

## Introduction PDF

Useful foundations:

- the course staircase: Python → data manipulation → preprocessing/feature engineering → machine learning → deep learning → MLOps → AI application;
- Python as a high-level, interpreted, general-purpose language;
- Jupyter and code editors like Cursor as learning tools;
- the practical trade-off between Python's simplicity and raw execution speed.

Teaching improvements:

- historical popularity charts are treated as historical motivation, not current rankings;
- speed charts are presented as implementation- and workload-dependent, not as a universal rule;
- setup is separated from language concepts.

## `2_basics.ipynb`

Kept: printing, variables, assignment, naming, unpacking, and basic data types.

Corrected:

- string + integer concatenation now uses an f-string;
- invalid identifiers are shown as text examples instead of executable cells;
- case sensitivity and indentation errors are explained safely;
- missing tuple/list type checks were completed.

## `3_strings.ipynb`

Kept: indexing, slicing, case conversion, replacement, splitting, f-strings, membership, stripping, counting, and finding positions.

Improved:

- examples use clearer variable names;
- `find()` versus `index()` is explained;
- Unicode/Persian text is included.

## `4_List.ipynb`

Kept: creation, indexing, mutation, appending, inserting, slicing, loops, removal, counting, and sorting.

Corrected:

- list objects do not have `.find()`; use `.index()` or membership checks;
- `append()` versus `extend()` is taught explicitly;
- aliasing and copying are introduced to prevent common bugs.

## `5_Dict_Set.ipynb`

Kept: key/value access, updates, deletion, iteration, membership, set uniqueness, adding, removing, and frozen sets.

Corrected:

- `{}` creates an empty dictionary; `set()` creates an empty set;
- invalid `{,}` syntax was removed;
- `remove()` versus `discard()` is explained;
- immutable `frozenset` examples no longer call `.add()` as valid code.

## `6_Functions_File_ExceptionHandling.ipynb`

Kept: defining/calling functions, parameters, return values, file reading/writing/appending, and `try/except/else/finally`.

Improved:

- functions, files, and exceptions are separate lessons;
- invalid file mode `ra` is replaced by correct modes such as `r+` and `a+`;
- file examples use `pathlib`, UTF-8, and temporary/safe paths;
- exception handlers match the actual errors;
- broad bare `except:` is discouraged.

## `7_Operators.ipynb`

Kept: arithmetic, assignment, comparison, logical, identity, and membership operators.

Corrected:

- `==` is used for value equality;
- `is` is taught for object identity, especially `is None`;
- integer interning is not used as a teaching shortcut because it can mislead beginners.
