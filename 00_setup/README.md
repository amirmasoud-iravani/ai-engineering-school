# Section 0: Setup

Before we go into codes, we should prepare the necessary setup and environments.

## The four practical tools

- **Python** is our coding language.
- **VS Code or Cursor** is the place where we write and edit codes.
- **Jupyter Notebook or JupyterLab** is a scientific notebook where codes can have presetation and run one small box at a time.
- **Git/GitHub** is a time machine plus an online shelf for our project versions and the changes commited to them.

## First setup on Windows

Open PowerShell inside this repository and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

A browser page opens. Click `01_python`, then open the first notebook.

## Why use a seperate virtual environment?

Imagine every project has its own lunchbox. A virtual environment keeps one project's packages from spilling into another project's lunchbox.

## Next

Read `github_for_beginners.md`, then begin `01_python/README.md`.
