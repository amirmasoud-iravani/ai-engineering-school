# AI Engineering School

A beginner-friendly learning repository for moving from **Python fundamentals** to building and operating AI systems.

The repository is organized as a sequence of stages:

- each **folder** is one stage;
- each **notebook** is one lesson;
- each **code cell** is a small experiment;
- each **exercise or project** applies the ideas introduced in the lessons.

## Start here

1. Prepare the environment with `00_setup/README.md`.
2. Follow stages `01_python/` through `04_matplotlib/` in numerical order.
3. Run every notebook and change small values to test your understanding.
4. Complete exercises before reading their reference solutions.
5. Finish each stage's practice or project before moving forward.

## School map

```text
ai-engineering-school/
├── 00_setup/                 # Install the learning environment
├── 01_python/                # Python fundamentals
├── 02_numpy/                 # Numerical arrays for data and NLP
├── 03_pandas/                # Tabular data and cleaning
├── 04_matplotlib/            # Visualization and research figures
├── 05_data_preprocessing/    # Preparing data for models
├── 06_machine_learning/      # Classical ML
├── 07_deep_learning/         # Neural networks and PyTorch
├── 08_mlops/                 # Testing, deployment, monitoring
├── 09_ai_applications/       # APIs, apps, RAG, and agents
└── 10_projects/              # End-to-end portfolio projects
```

## Learning path

The completed path is:

```text
Python → NumPy arrays → pandas tables → Matplotlib visualizations
```

Stages `01`–`04` are complete. Stages `05`–`10` currently provide lesson maps for data preprocessing, machine learning, deep learning, MLOps, AI applications, and end-to-end projects.

## Run the notebooks

From the repository folder in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Then open `01_python/README.md` and continue in numerical order.

## Learning rule

Completed stages follow this general pattern:

> small idea → worked example → checkpoint or exercise → application

Large technical skills grow through small, connected steps.
