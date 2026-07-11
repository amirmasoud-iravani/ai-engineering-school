# AI Engineering School

A beginner-friendly learning repository for moving from **Python basics** to building and operating AI systems.

Think of this repository as a school made of rooms:

- Each **folder** is a classroom.
- Each **notebook** is a lesson book.
- Each **code cell** is a little experiment button.
- Each **project** is a toy you build from the pieces you learned.

## Start here

1. Open `00_setup/README.md`.
2. Study `01_python/` in numerical order.
3. Run the notebooks yourself. Reading code without running it is like reading about swimming without touching water.
4. Complete the exercises before looking at the solutions.
5. Build the Python mini-project.

## School map

```text
ai-engineering-school/
├── 00_setup/                 # Install tools and learn the repository
├── 01_python/                # Current complete module
├── 02_numpy/                 # Numerical arrays
├── 03_pandas/                # Tables and data cleaning
├── 04_matplotlib/            # Data visualization
├── 05_data_preprocessing/    # Preparing data for models
├── 06_machine_learning/      # Classical ML
├── 07_deep_learning/         # Neural networks and PyTorch
├── 08_mlops/                 # Testing, deployment, monitoring
├── 09_ai_applications/       # APIs, apps, RAG, and agents
└── 10_projects/              # End-to-end portfolio projects
```

## Why this structure?

The course introduction presents a staircase from Python to data work, preprocessing and feature engineering, machine learning, deep learning, MLOps, and AI applications. This repository follows that staircase while adding setup, testing, projects, and a separate data-preprocessing stage.

## What is ready now?

The **Python classroom** is ready. The later classrooms contain carefully planned lesson maps so the repository can grow without becoming messy.

## Run the notebooks

From the repository folder:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

Then open `01_python/README.md`.

## Learning rule

Every lesson follows this pattern:

> tiny idea → tiny code → tiny exercise → small project

That is how large skills are built: one small block at a time.
