# Setup & Troubleshooting

This document explains how to set up the project environment and resolves common issues you may encounter (missing imports, pyarrow build errors, NLTK data).

## 1 — Recommended (pip + venv)

1. Open PowerShell in the project root.
2. Run the bundled script (recommended):

```powershell
./scripts/setup_env.ps1
```

This will create `.venv`, install packages from `requirements.txt`, and download NLTK stopwords.

## 2 — Quick manual steps (if you prefer)

```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r .\requirements.txt
python -c "import nltk; nltk.download('stopwords')"
```

## 3 — If pip fails building some packages (e.g. `pyarrow`)

- Option A (easiest): use conda/Miniconda and install binary packages from `conda-forge`:

```powershell
# install miniconda (if needed) then:
conda create -n sentiment python=3.10 -y
conda activate sentiment
conda install -c conda-forge --file requirements.txt
```

- Option B (build from source on Windows): install required build tools (CMake + Visual Studio Build Tools):

```powershell
winget install --id Kitware.CMake -e
winget install --id Microsoft.VisualStudio.2022.BuildTools -e
# then retry pip install
python -m pip install -r requirements.txt
```

## 4 — VS Code Pylance unresolved import tips

- Ensure VS Code uses the same Python interpreter where you installed packages:
  - Ctrl+Shift+P → `Python: Select Interpreter` → choose the `.venv` interpreter shown by `python -c "import sys; print(sys.executable)"`.
  - Reload window: Ctrl+Shift+P → `Developer: Reload Window`.
  - Restart language server: Ctrl+Shift+P → `Python: Restart Language Server`.

## 5 — NLTK data

The app requires `stopwords`. If you see errors regarding `stopwords`, run:

```powershell
python -c "import nltk; nltk.download('stopwords')"
```

## 6 — Running the app

- Start the Flask API (optional):

```powershell
python api.py
# or
flask --app api.py run --port=5000
```

- Start the Streamlit UI:

```powershell
streamlit run main.py
```

If Streamlit is deployed somewhere that cannot access `127.0.0.1:5000`, the Streamlit app will automatically fall back to local model predictions (it imports `predict_sentiment` from `api.py`).

## 7 — Further help

If you get an installation error, paste the full pip output here and I'll help diagnose (include your `python -V` output).