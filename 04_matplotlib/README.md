# Stage 4: Matplotlib

This stage turns NumPy arrays and pandas tables into clear, reproducible visualizations. It begins with general plotting foundations and then applies them to Persian corpus linguistics, NLP annotation, model evaluation, and research reporting.

## Prerequisite

Complete `../03_pandas/README.md`. You should be comfortable selecting, grouping, and summarizing table columns before plotting them.

## Learning path

1. **`01_matplotlib_foundations.ipynb`**
   - `Figure`/`Axes` object model
   - line, bar, grouped/stacked bar, scatter, histogram, box, violin, and donut plots
   - labels, titles, legends, annotations, reference lines, subplots, log scales
   - color accessibility and common plotting mistakes
   - dedicated `Series.plot()` and `DataFrame.plot()` coverage
   - publication-ready PNG, SVG, and PDF export
   - exercises with executable reference solutions

2. **`02_corpus_nlp_visualization.ipynb`**
   - corpus balance and document-length distributions
   - Zipf plots, vocabulary growth, and lexical diversity
   - POS and annotation-label distributions
   - learner-error heatmaps, metaphor rates, and temporal trends
   - Persian/right-to-left labels and concordance-style displays
   - corpus-focused exercises with executable solutions

3. **`03_nlp_evaluation_research_figures.ipynb`**
   - annotation status and annotator confusion
   - classification confusion matrices and per-class metrics
   - model comparisons with uncertainty and paired runs
   - learning curves, thresholds, calibration, and residual analysis
   - error slices, embedding projections, and publication multi-panels
   - evaluation exercises with executable solutions

4. **`04_guided_project_persian_corpus_report.ipynb`**
   - complete end-to-end small project
   - synthetic document-level Persian corpus data
   - data-quality audit and corpus balance analysis
   - normalized metaphor and learner-error rates
   - emotion trends and a final four-panel report
   - written interpretation and PNG/SVG/PDF export
   - extension exercises with reference solutions

## Learning pattern

Each teaching notebook combines explanations, self-contained synthetic data, runnable examples, exercises, and reference solutions. The final notebook integrates those skills in a guided Persian corpus report.

## What you should be able to do afterward

- choose a chart that matches the data and research question;
- use the object-oriented `Figure` and `Axes` interface;
- visualize corpus composition, distributions, annotation, and NLP evaluation;
- state units, normalization, uncertainty, and scale choices clearly;
- create multi-panel research figures and export them in raster and vector formats.

## Recommended order

Run the notebooks in numerical order. Complete the exercises before reading the reference solutions. No external dataset is required.

## Core dependencies

```text
pip install matplotlib numpy pandas
```

Optional Persian/Arabic text shaping:

```text
pip install arabic-reshaper python-bidi
```

## Next stage

The completed foundation ends here. Continue with the planned lessons in `../05_data_preprocessing/README.md` when that stage is developed.
