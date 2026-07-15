# NumPy source review and improvements

The three uploaded notebooks were carefully reviewed and used as foundations. Their useful content was
preserved, reorganized, corrected, and expanded into a coherent lesson sequence.

## Material preserved

- importing NumPy and checking the version;
- creating 1D, 2D, and 3D arrays;
- `ndim`, `shape`, `size`, and `dtype`;
- `zeros`, `ones`, `full`, `arange`, and `linspace`;
- type conversion with `astype`;
- indexing in one, two, and three dimensions;
- slicing, views, and copies;
- reshape;
- sum, mean, variance, standard deviation, product, minimum, and maximum;
- aggregation by axis.

## Corrections

1. A 12-element array cannot be reshaped to `(4, 4)`. The revised lesson demonstrates the error safely
   and explains that the total number of elements must stay unchanged.
2. One saved output in the second source notebook reported a 3D shape for a 2D array, probably because
   the notebook had been run out of order. The rewritten notebooks are executed from top to bottom so
   saved outputs match the code.
3. The view/copy source notebook contained a later `b` output that did not match the immediately
   preceding copy example, again suggesting stale notebook state. The new lesson resets variables and
   makes the difference explicit.
4. The external introductory image was removed so every lesson works offline and avoids depending on a
   third-party URL.
5. Comments such as “axis 0 means columns” were replaced with the more general rule that aggregation
   removes the selected axis. This rule continues to work for 3D and higher-dimensional arrays.
6. Examples now use clear names rather than repeatedly reusing `a`, `b`, `h`, and `u` across unrelated
   concepts.

## Added material

- comparisons with Python lists and a small timing demonstration;
- memory properties (`itemsize`, `nbytes`);
- Boolean masks, compound conditions, and fancy indexing;
- `ravel`, `flatten`, transpose, new axes, squeeze, concatenate, and stack;
- vectorization, broadcasting rules, ufuncs, and `np.where`;
- `argmin`, `argmax`, percentiles, `keepdims`, `ddof`, and NaN-aware statistics;
- NumPy's modern `default_rng` API and reproducible splitting;
- dot products, matrix multiplication, norms, cosine similarity, and linear systems;
- a Persian NLP lesson covering token IDs, padding, masks, count matrices, and embeddings;
- exercises, solutions, and a tested embedding-similarity mini-project.
