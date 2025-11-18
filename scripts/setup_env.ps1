# PowerShell setup script for sentiment_amazon.web
# Run from project root: ./scripts/setup_env.ps1

param(
    [switch]$UseConda
)

if ($UseConda) {
    Write-Host "Conda requested — create a conda env instead." -ForegroundColor Cyan
    Write-Host "Run: conda create -n sentiment python=3.10 -y" -ForegroundColor Green
    Write-Host "Then activate: conda activate sentiment" -ForegroundColor Green
    Write-Host "Then run: conda install -c conda-forge --file requirements.txt" -ForegroundColor Green
    exit 0
}

# Create virtualenv
Write-Host "Creating virtual environment .venv..." -ForegroundColor Cyan
python -m venv .venv

# Allow script to run for this session
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force

# Activate
Write-Host "Activating virtual environment..." -ForegroundColor Cyan
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install requirements
Write-Host "Upgrading pip and installing requirements..." -ForegroundColor Cyan
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r .\requirements.txt

# Download NLTK data (stopwords)
Write-Host "Downloading NLTK stopwords..." -ForegroundColor Cyan
python -c "import nltk; nltk.download('stopwords')"

Write-Host "Setup complete. To run Streamlit: streamlit run main.py" -ForegroundColor Green
Write-Host "To run Flask API: python api.py" -ForegroundColor Green
