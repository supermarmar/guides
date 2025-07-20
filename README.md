# Project Organization

```text
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── mappings       <- Data dictionaries.
│   ├── predictions    <- Model predictions for both training and testing.
│   ├── processed      <- The **final**, canonical data sets for modeling.
│   ├── raw            <- The original, immutable data dump.
│   └── template       <- Standardised Excel templates used for client engagements or model inputs.
│
├── docs               <- Version-controlled guides, including executable examples and a bibliography
│   ├── azure          <- An Azure specific guide with team standards on managing the repo
│   ├── modelling      <- Training and reference guides for all topics (e.g. IFRS 9, Basel 3.1)
│   └── regulation     <- Latest regulation material for IFRS9, Basel 3.1, PRA etc.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         src and configuration for tools like black
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8.
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes src a Python module.
    │
    ├── config.py               <- Store useful variables and configuration.
    │
    └── functions               <- Store all functions that get imported into pipelines.
```

## Documentation

For detailed information, please refer to the [documentation](docs/index.md).

## Packages

```python
# visualisation
matplotlib # 2D plotting library.
seaborn # Statistical data visualization based on matplotlib.
plotly # Interactive plotting library.

# data manipulation
numpy # Numerical computing foundation.
pandas # Data manipulation and analysis.
polars # Blazingly fast DataFrames.
pyarrow #Apache Arrow for columnar data processing using parquet.

# data validation
pandera # Data validation and schema enforcement for pandas DataFrames.

# data generation & API
faker # Generate synthetic data for testing and development.
eikon # Refinitiv Eikon API for financial data (assuming this is the intended use).

# database
duckdb # In-process analytical SQL database.
psycopg # PostgreSQL adapter for Python.
sqlparse # SQL parser for Python.
pyspark # Apache Spark interface for Python (Big Data processing).

# stats models
scipy # Scientific computing, including statistics, optimization, etc.
statsmodels # Statistical models, hypothesis testing, and data exploration.

# ml models
scikit-learn # General machine learning algorithms.
xgboost # Gradient boosting library.
lightgbm
catboost

# alternative models
lifelines # Survival analysis.
nelson-siegel-svensson # Library for Nelson-Siegel-Svensson yield curve fitting.

# natural language processing
nltk # Natural Language Toolkit.
spacy

# model interpretability
lime
shap

# utility
tqdm # Progress bars for loops and iterables.
loguru # Logging library.
dotenv # Load environment variables from .env files.
typer # Build command-line interfaces easily.
ipykernel # IPython kernel for Jupyter notebooks and interactive computing.
papermill # Tool for parameterizing and executing Jupyter Notebooks.
```
