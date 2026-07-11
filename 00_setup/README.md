# Room 0: Setup

Before we play with code, we prepare the table.

## The four tools

- **Python** is the language.
- **VS Code or Zed** is the desk where you edit files.
- **JupyterLab** is a science notebook where code runs one small box at a time.
- **Git/GitHub** is a time machine plus an online shelf for your project.

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

## Why use a virtual environment?

Imagine every project has its own lunchbox. A virtual environment keeps one project's packages from spilling into another project's lunchbox.

## Next

Read `github_for_beginners.md`, then begin `01_python/README.md`.
