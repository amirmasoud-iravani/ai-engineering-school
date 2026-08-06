# Stage 5: Data preprocessing

This stage turns raw tables and text into reproducible, model-ready features. It is the bridge between pandas/Matplotlib analysis and the estimators introduced in Stage 6.

## Prerequisite

Complete `../04_matplotlib/README.md`. You should be comfortable auditing pandas tables, working with NumPy arrays, and interpreting data distributions before transforming them.

## Learning path

1. [`00_why_preprocessing.ipynb`](00_why_preprocessing.ipynb) — feature roles, learned transformations, `fit`/`transform`, and the boundary with machine learning
2. [`01_data_audit_and_feature_definition.ipynb`](01_data_audit_and_feature_definition.ipynb) — prediction units, data contracts, missingness, duplicates, ranges, identifiers, and audit-only variables
3. [`02_splitting_and_leakage.ipynb`](02_splitting_and_leakage.ipynb) — train/validation/test partitions, stratification, learner groups, duplicate clusters, time splits, and leakage
4. [`03_missing_values_and_outliers.ipynb`](03_missing_values_and_outliers.ipynb) — structural missingness, imputation, indicators, outlier flags, and robust scaling
5. [`04_encoding_scaling_and_transformations.ipynb`](04_encoding_scaling_and_transformations.ipynb) — nominal/ordinal encoding, scaling, log transforms, and polynomial features
6. [`05_feature_engineering_and_selection.ipynb`](05_feature_engineering_and_selection.ipynb) — transparent features, forbidden columns, variance filtering, and train-fitted supervised selection
7. [`06_pipelines_and_column_transformer.ipynb`](06_pipelines_and_column_transformer.ipynb) — numerical and categorical pipelines, mixed columns, stable output schemas, and feature names
8. [`07_text_preprocessing_for_persian_nlp.ipynb`](07_text_preprocessing_for_persian_nlp.ipynb) — aligned text views, Persian Unicode normalization, duplicate detection, and word/character TF–IDF
9. [`exercises/01_preprocessing_exercises.ipynb`](exercises/01_preprocessing_exercises.ipynb) — independent practice
10. [`exercises/solutions/01_preprocessing_solutions.ipynb`](exercises/solutions/01_preprocessing_solutions.ipynb) — reference solutions after practice
11. [`projects/learner_corpus_preprocessor/01_learner_corpus_preprocessor.ipynb`](projects/learner_corpus_preprocessor/01_learner_corpus_preprocessor.ipynb) — complete learner-corpus preprocessing project

## Central rule

> split first → fit preprocessing on training data → reuse it on validation/test data

Deterministic validation and normalization rules may be defined in advance, but medians, category vocabularies, scaling statistics, TF–IDF weights, and target-aware feature selectors must be learned from training data only.

## Persian NLP principle

Preserve the raw text. Create aligned normalized and analysis-oriented views instead of destructively overwriting it. Keep emojis, hashtags, punctuation, repetition, code-mixing, and other potentially meaningful signals unless the research question justifies removing them.

## What you should be able to do afterward

- define a prediction unit, target, feature set, identifiers, split groups, and audit-only variables;
- select a split strategy that matches independent, grouped, duplicated, or temporal data;
- prevent target, test-set, participant, document, and duplicate leakage;
- handle numerical, categorical, and textual features with training-fitted transformations;
- build a `ColumnTransformer`/`Pipeline` with a stable feature schema;
- produce model-ready train, validation, and test matrices with documented checks.

## Boundary with Stage 6

This stage does not teach linear regression, logistic regression, metrics, regularization, or model selection. Those topics begin in `../06_machine_learning/README.md`, where estimators will be attached to the preprocessing pipelines built here.
