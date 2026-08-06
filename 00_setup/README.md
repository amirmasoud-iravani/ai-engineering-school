# Stage 0: Setup

Prepare a clean learning environment before writing code.

## The three practical tools

- **Python** runs the code.
- **VS Code or Cursor** provides an editor for notebooks, scripts, and text files.
- **JupyterLab** combines explanations, code, and results in cells that can be run one at a time.

## First setup on Windows

Open PowerShell inside this repository and run:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

A browser page opens. Select `01_python`, read its `README.md`, and open the first notebook.

## Why use a separate virtual environment?

Imagine every project has its own lunchbox. A virtual environment keeps one project's packages from spilling into another project's lunchbox.

## Next

Begin with `01_python/README.md`.
