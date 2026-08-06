# Stage 2: NumPy

This stage turns Python sequences into efficient numerical arrays and connects them to machine learning, Persian NLP, and the later pandas stage.

## Prerequisite

Complete `../01_python/README.md`, including its exercises and text-analyzer project.

## Recommended order

1. [`00_why_numpy.ipynb`](00_why_numpy.ipynb) — lists, arrays, vectorization, and use cases
2. [`01_arrays_creation_and_properties.ipynb`](01_arrays_creation_and_properties.ipynb) — dimensions, shapes, sizes, dtypes, and constructors
3. [`02_indexing_slicing_masks.ipynb`](02_indexing_slicing_masks.ipynb) — selecting data, views, copies, masks, and fancy indexing
4. [`03_shapes_reshape_and_combine.ipynb`](03_shapes_reshape_and_combine.ipynb) — reshape, transpose, new axes, concatenation, and stacking
5. [`04_vectorization_and_broadcasting.ipynb`](04_vectorization_and_broadcasting.ipynb) — array arithmetic, broadcasting, ufuncs, and matrix multiplication
6. [`05_aggregations_axes_and_statistics.ipynb`](05_aggregations_axes_and_statistics.ipynb) — sums, means, axes, variance, percentiles, and NaN
7. [`06_random_numbers_and_reproducibility.ipynb`](06_random_numbers_and_reproducibility.ipynb) — the modern random generator and reproducible experiments
8. [`07_linear_algebra_for_ml.ipynb`](07_linear_algebra_for_ml.ipynb) — dot products, matrix multiplication, norms, cosine similarity, and solving systems
9. [`08_numpy_for_nlp.ipynb`](08_numpy_for_nlp.ipynb) — token IDs, padding, masks, document-term matrices, and embeddings
10. [`exercises/01_numpy_exercises.ipynb`](exercises/01_numpy_exercises.ipynb) — independent practice
11. [`exercises/solutions/01_numpy_solutions.ipynb`](exercises/solutions/01_numpy_solutions.ipynb) — solutions after practice
12. [`projects/embedding_similarity/01_embedding_similarity_project.ipynb`](projects/embedding_similarity/01_embedding_similarity_project.ipynb) — a small portfolio project

## Learning pattern

> small idea → worked example → checkpoint → NLP connection → project

## What you should be able to do afterward

- explain an array's `shape`, `ndim`, `size`, and `dtype`;
- select and reshape data without confusing views and copies;
- replace simple numerical loops with vectorized operations;
- reason about broadcasting and axes;
- produce reproducible random samples;
- perform basic linear algebra;
- represent simple NLP data numerically.

## Study rule

Open this folder in JupyterLab and study the notebooks in numerical order. Predict array shapes before running cells, especially when indexing, reshaping, broadcasting, or aggregating across axes.

## Next stage

Continue to `../03_pandas/README.md` to work with labeled tables, missing values, and corpus metadata.
