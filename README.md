# UK CRM Credit Risk Library

Welcome to the UK CRM Credit Risk Library. The purpose of this library is to create, review and maintain valuable code related to credit modelling engagements, for the benefit and continued development of team members.

Contributing to this Library should be a rewarding experience that can enhance your skills and benefit the community. By adhering to these guidelines, you can contribute responsibly while safeguarding client confidentiality and upholding professional ethics.

Everyone in the team is welcome to contribute to this library!

## Project Organization

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
│   ├── modelling      <- Training and reference guides for all CRM topics (e.g. IFRS 9, Basel 3.1)
│   └── regulation     <- Latest regulation material for IFRS9, Basel 3.1, PRA etc.
│
├── pipelines          <- Automated pipelines run using papermill to execute notebooks.
│
├── playground         <- Playground where team members can code freely and contribute to the repo.
│   ├── clients        <- Code written during projects.
│   └── template       <- Folder structure template for all projects.
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
    └── functions               <- Store all functions that get imported into pipelines and originate from playground.
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

# utility
tqdm # Progress bars for loops and iterables.
loguru # Logging library.
dotenv # Load environment variables from .env files.
typer # Build command-line interfaces easily.
ipykernel # IPython kernel for Jupyter notebooks and interactive computing.
papermill # Tool for parameterizing and executing Jupyter Notebooks.
```

## Benefits of contributing to the library

- **Enhanced Skills**: Working on real-world projects exposes you to diverse coding styles, problem-solving approaches, and cutting-edge technologies, enhancing your technical expertise.
- **Knowledge Sharing**: Contributing fosters a culture of collaboration and knowledge exchange, benefiting both individual contributors and the wider team.
- **Giving Back**: The library thrives on contributions. By participating, you contribute to solutions used by many.

## Risks and considerations for consultants

- **Client Confidentiality**: Protecting client data and intellectual property is paramount. Never copy code from client projects into open source repositories, and exercise extreme caution when implementing solutions inspired by open source projects for clients.
- **Time Management**: Contributing requires dedicated time and effort. Ensure you balance contributions with client commitments and internal responsibilities.
- **Code Quality and Licensing**: Adhere to the project's coding standards and licensing agreements. Ensure your contributions meet the required quality and legal standards.

## Best Practices for Responsible Contribution

- **Start Small**: Begin with contributions like bug fixes, documentation improvements, or adding unit tests to familiarise yourself with the project's work flow.
- **Choose Projects Wisely**: Focus on projects relevant to your expertise in Credit Risk.
- **Understand Project Guidelines**: Thoroughly review the project's contributing guidelines, and coding style.
- **Communication is Key**: Engage with the project maintainers and community. Ask questions, seek clarification, and participate in discussions.
- **Respect Intellectual Property**: Never copy code from clients or other sources.
- **Seek Internal Guidance**: Consult with Rohan or Will if you have any questions.

## Protecting Client Confidentiality

- **Clean Room Approach**: When drawing inspiration from open source for client solutions, implement a "clean room" approach. This involves re-implementing the concept from scratch based on your understanding, ensuring no direct code copying.
- **Code Reviews**: Implement rigorous code reviews within your team to identify and mitigate any potential risks of inadvertently including client-specific code in open source contributions.
