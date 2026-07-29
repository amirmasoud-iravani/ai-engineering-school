# 04_matplotlib — Data Visualization for NLP and Corpus Linguistics

A complete Matplotlib module for the `ai-engineering-school` repository. It teaches general visualization foundations and applies them to Persian corpus linguistics, NLP annotation, model evaluation, and research reporting.

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

## Completion rule coverage

Every requirement is now represented:

- **Explanations:** Markdown lessons explain chart choice, units, normalization, uncertainty, and interpretation.
- **Runnable notebooks:** All notebooks are self-contained and use deterministic synthetic data.
- **Exercises:** Each teaching notebook includes explicit tasks.
- **Solutions:** Exercise sections include executable cells tagged `solution`.
- **Small project:** Notebook 04 is a complete guided project with deliverables and exports.

## Planned lesson checklist

- [x] figures and axes
- [x] line, bar, scatter, and histogram plots
- [x] labels, titles, legends, and annotations
- [x] plotting pandas data
- [x] saving publication-ready figures

## Recommended order

Run the notebooks in numerical order. No external dataset is required.

## Core dependencies

```bash
pip install matplotlib numpy pandas
```

Optional Persian/Arabic text shaping:

```bash
pip install arabic-reshaper python-bidi
```

## Notes

- All teaching datasets and reported values are synthetic.
- Replace generated DataFrames with versioned project data when adapting the notebooks.
- The notebooks favor Matplotlib's explicit object-oriented `Figure`/`Axes` interface.
- Generated figures are written to a local `figures/` folder, which you may add to `.gitignore` if you do not want to commit rendered outputs.
