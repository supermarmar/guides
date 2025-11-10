from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = PROJ_ROOT / "data"
DATABASE_DIR = DATA_DIR / "database"

RAW_DATA_DIR = DATA_DIR / "raw"
DUMMY_DATA_DIR = RAW_DATA_DIR / "dummy"
KAGGLE_DATA_DIR = RAW_DATA_DIR / "kaggle"
HOME_CREDIT_DATA_DIR = KAGGLE_DATA_DIR / "home_credit_group"
AMEX_DATA_DIR = KAGGLE_DATA_DIR / "amex"
CREDIT_RISK_DATA_DIR = KAGGLE_DATA_DIR / "credit_risk"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXTERNAL_DATA_DIR = DATA_DIR / "external"
MODELS_DIR = PROJ_ROOT / "models"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

HOME_CREDIT_DB = "home_credit_mds.db"
DATA_DICTIONARY_FILE = "HomeCredit_columns_description.csv"
