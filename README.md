# Credit Risk Modelling Guide

**A comprehensive learning resource for aspiring credit risk modellers, covering everything from fundamental concepts to advanced regulatory model development.**

This repository provides a structured pathway to becoming a proficient credit risk modeller, featuring practical guides, executable code examples, and real-world applications of regulatory frameworks including IFRS 9 impairment modelling and Advanced Internal Ratings-Based (A-IRB) capital models.

## 🎯 Learning Journey

### **Foundation Level** → **Intermediate** → **Advanced Regulatory Models**

1. **Fundamentals** (`docs/fundamentals/`): Master core skills in programming, statistics, and machine learning
2. **Credit Risk Theory** (`docs/credit_risk_modelling/`): Learn domain-specific concepts and regulatory frameworks  
3. **Practical Implementation**: Build production-ready models following industry best practices
4. **Regulatory Compliance**: Implement IFRS 9, Basel III/IV, and supervisory requirements

## 📁 Repository Structure

```text
├── LICENSE            <- Open-source license
├── Makefile           <- Automation commands for data processing and model training
├── README.md          <- This comprehensive guide to the repository
├── data               <- Structured data organization for model development
│   ├── external       <- Third-party datasets (e.g., macroeconomic indicators)
│   ├── interim        <- Intermediate processed datasets
│   ├── mappings       <- Data dictionaries and schema definitions
│   ├── predictions    <- Model outputs for validation and testing
│   ├── processed      <- Clean, model-ready datasets (CCD - Cleaned Consolidated Data)
│   ├── raw            <- Original, immutable source data
│   └── template       <- Standardized templates for client deliverables
│
├── docs               <- 📚 **Main Learning Content** - Interactive guides and examples
│   ├── fundamentals   <- 🎓 Core skills: Python, SQL, Statistics, ML fundamentals
│   │   ├── 01_software_engineering    <- Coding standards, version control, best practices  
│   │   ├── 02_data_engineering       <- Data manipulation, validation, pipeline design
│   │   ├── 03_data_analysis          <- Pandas, visualization, exploratory analysis
│   │   ├── 04_mathematics            <- Linear algebra, calculus foundations
│   │   ├── 05_statistics             <- Probability, inference, time series analysis
│   │   └── 06_machine_learning       <- Supervised/unsupervised learning, model evaluation
│   │
│   ├── credit_risk_modelling  <- 🏦 Domain-specific credit risk applications
│   │   ├── a-irb_capital_modelling   <- Advanced IRB models for regulatory capital
│   │   │   ├── 01_introduction       <- Economic capital, systemic risk concepts
│   │   │   ├── 02_data_engineering   <- Data quality assessment (BCBS 239 compliance)
│   │   │   └── 03_portfolio_description <- Segmentation and descriptive analytics
│   │   ├── ifrs9_impairment_modelling <- IFRS 9 Expected Credit Loss models
│   │   └── climate                    <- Climate risk stress testing and scenarios
│   │
│   ├── regulation     <- 📋 Regulatory frameworks and compliance requirements
│   │   ├── international <- Basel Framework, BCBS 239, IFRS 9 standards
│   │   ├── eu           <- European regulations (CRR, EBA guidelines)
│   │   └── uk           <- UK-specific requirements (PRA, Bank of England)
│   │
│   └── azure          <- ☁️ Cloud deployment and team collaboration standards
│
├── pyproject.toml     <- Python project configuration and dependency management
├── requirements.txt   <- Reproducible environment setup
├── setup.cfg          <- Code quality and linting configuration
│
└── src               <- 🔧 Reusable source code and utilities
    ├── __init__.py   <- Python package initialization
    ├── config.py     <- Configuration management and constants
    └── functions     <- Modular functions for data processing and modeling
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ with virtual environment management
- Basic understanding of statistics and programming concepts
- Interest in financial risk management and regulatory compliance

### Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd guides

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start with fundamentals
jupyter notebook docs/fundamentals/01_software_engineering/01-coding-standards.md
```

## 📖 Learning Pathways

### 🎓 **Path 1: Complete Beginner**

**For those new to both programming and finance**

1. **Software Engineering Basics** (`docs/fundamentals/01_software_engineering/`)
   - Coding standards and best practices
   - Version control with Git
   - Jupyter notebook workflows

2. **Data Foundation** (`docs/fundamentals/02_data_engineering/`)
   - Data manipulation with pandas
   - Data validation with pandera
   - Database management with SQL/DuckDB

3. **Statistical Foundation** (`docs/fundamentals/05_statistics/`)
   - Descriptive and inferential statistics
   - Probability theory and distributions
   - Time series analysis

### 💼 **Path 2: Finance Professional**

**For finance professionals needing technical skills**

1. **Quick Technical Onboarding**
   - Python essentials (`docs/fundamentals/03_data_analysis/`)
   - Machine learning fundamentals (`docs/fundamentals/06_machine_learning/`)

2. **Credit Risk Implementation**
   - IFRS 9 impairment models (`docs/credit_risk_modelling/ifrs9_impairment_modelling/`)
   - Regulatory compliance (`docs/regulation/`)

### 🔬 **Path 3: Data Scientist**

**For data scientists needing domain expertise**

1. **Credit Risk Domain Knowledge**
   - Economic capital concepts (`docs/credit_risk_modelling/a-irb_capital_modelling/01_introduction/`)
   - Regulatory frameworks (`docs/regulation/`)

2. **Specialized Applications**
   - Advanced IRB modelling
   - Climate risk stress testing

## 🏗️ Key Features

### **Interactive Learning**

- ✅ **Executable Notebooks**: All concepts demonstrated with working code
- ✅ **Real-world Datasets**: Practice with actual credit portfolio data
- ✅ **Regulatory Examples**: IFRS 9 and Basel III/IV implementations

### **Industry Standards**

- ✅ **BCBS 239 Compliance**: Data quality assessment frameworks
- ✅ **Model Risk Management**: Validation and governance practices
- ✅ **Production Ready**: Scalable code architecture and deployment patterns

### **Comprehensive Coverage**

- ✅ **End-to-End Pipeline**: From raw data to regulatory reporting
- ✅ **Multiple Frameworks**: IFRS 9, Basel III/IV, climate risk
- ✅ **Best Practices**: Industry-standard methodologies and validation techniques

## 📚 Core Topics Covered

### **Technical Foundations**

| Topic | Description | Key Tools |
|-------|-------------|-----------|
| **Data Engineering** | ETL pipelines, quality assessment, schema validation | pandas, pandera, DuckDB |
| **Statistical Modeling** | GLMs, survival analysis, time series | scipy, statsmodels, lifelines |
| **Machine Learning** | Feature engineering, model selection, validation | scikit-learn, XGBoost, SHAP |
| **Model Interpretation** | LIME, SHAP, model-agnostic explanations | lime, shap, plotly |

### **Credit Risk Applications**

| Model Type | Regulatory Framework | Implementation |
|------------|---------------------|----------------|
| **PD Models** | Basel III/IV Advanced IRB | Logistic regression, survival models |
| **LGD Models** | Basel III/IV Advanced IRB | Beta regression, machine learning |
| **EAD Models** | Basel III/IV Advanced IRB | Linear regression, time-to-default |
| **ECL Models** | IFRS 9 Expected Credit Loss | Multi-stage lifetime loss modeling |
| **Stress Testing** | CCAR, ICAAP, Climate Risk | Scenario analysis, econometric models |

### **Regulatory Compliance**

- **Data Quality**: BCBS 239 principles and implementation
- **Model Governance**: SR 11-7, SS1/18 supervisory expectations  
- **Validation Framework**: Independent validation and use test requirements
- **Documentation**: Model Risk Management and regulatory submission standards

## 🛠️ Technology Stack

### **Core Data Science Libraries**

```python
# Data Manipulation & Analysis
pandas          # Primary data manipulation and analysis
polars          # High-performance DataFrame operations  
numpy           # Numerical computing foundation
pyarrow         # Columnar data processing with Parquet

# Data Validation & Quality
pandera         # Schema validation and data quality enforcement

# Visualization & Reporting  
matplotlib      # Core plotting functionality
seaborn         # Statistical data visualization
plotly          # Interactive charts and dashboards

# Database & Storage
duckdb          # In-process analytical SQL database
psycopg         # PostgreSQL connectivity
sqlparse        # SQL parsing and formatting
pyspark         # Big data processing with Apache Spark
```

### **Statistical & Machine Learning**

```python
# Statistical Analysis
scipy           # Scientific computing and statistics
statsmodels     # Econometric and statistical models
lifelines       # Survival analysis for time-to-default models

# Machine Learning
scikit-learn    # General-purpose ML algorithms
xgboost         # Gradient boosting for credit scoring
lightgbm        # Efficient gradient boosting
catboost        # Categorical feature handling

# Model Interpretation & Explainability  
shap            # Model explanation and feature importance
lime            # Local interpretable model explanations

# Specialized Financial Models
nelson-siegel-svensson  # Yield curve modeling
```

### **Development & Production**

```python
# Workflow & Automation
papermill       # Parameterized notebook execution
typer           # CLI application development
tqdm            # Progress tracking for long operations

# Data Generation & Testing
faker           # Synthetic data generation for testing

# Logging & Monitoring
loguru          # Structured logging and monitoring

# Environment Management
python-dotenv   # Environment variable management
```

## 🤝 Contributing

We welcome contributions from the credit risk modelling community! Whether you're:

- **Sharing expertise** in regulatory frameworks
- **Adding new examples** or use cases  
- **Improving documentation** and explanations
- **Fixing bugs** or enhancing existing code

Please see our [contribution guidelines](docs/azure/02_contribution.md) for details on how to get involved.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋 Support & Community

- **Issues**: Report bugs or request features via [GitHub Issues](../../issues)
- **Discussions**: Join the conversation in [GitHub Discussions](../../discussions)
- **Documentation**: Comprehensive guides available in the [`docs/`](docs/) directory

## 📈 Learning Outcomes

Upon completing this guide, you will be able to:

- ✅ **Build production-ready credit risk models** following industry best practices
- ✅ **Implement regulatory frameworks** including IFRS 9 and Basel III/IV
- ✅ **Apply advanced statistical techniques** to real-world credit portfolios  
- ✅ **Validate and govern models** according to supervisory expectations
- ✅ **Deploy scalable solutions** using modern data engineering practices
- ✅ **Navigate regulatory requirements** and compliance frameworks confidently

---

**Ready to start your credit risk modelling journey?** 🎯

Begin with the [fundamentals](docs/fundamentals/) and work your way up to building sophisticated [regulatory models](docs/credit_risk_modelling/)!
