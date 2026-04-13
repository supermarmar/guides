---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/application-scorecards/feature-engineering/sampling
  - difficulty/unknown
  - study-status/new
aliases:
---
# Splits

In credit risk modeling, banks often create training, testing, and holdout datasets instead of just the typical train-test split because of the high-stakes nature of credit decisions, regulatory requirements, and the need to ensure robust and unbiased model performance over time. 

1. **Training Dataset (50%)**: Used to train the model by finding the optimal parameters that minimize prediction errors.
2. **Testing Dataset (30%)**: Used to evaluate the model's performance during development. It is used to tune [[01-hyperparamter-tuning|hyperparameters]] and evaluate intermediate iterations of the model.
3. **Holdout Dataset (20%)**: A completely independent dataset reserved until the final stages of model development. Acts as a proxy for future data to validate how the model will perform in real-world scenarios. It provides a final unbiased assessment of model performance.

Regulatory bodies often require banks to demonstrate that the model has been tested on independent data that was not used in any way during training or tuning. The holdout dataset is a key part of this evidence. The holdout dataset simulates this scenario, providing insight into how well the model will perform on new customers.

Credit risk models often remain in use for years. The holdout dataset can be used to assess whether the model is stable over time, especially if the holdout data is drawn from a later time period.

## Sampling Methods

Sampling methods are techniques used to select a subset of individuals or items (a sample) from a larger population for analysis. 

1. **Probability Sampling** 

In probability sampling, every member of the population has a known and non-zero chance of being selected. 
- Simple Random Sampling: Each member of the population has an equal chance of being selected.
- Stratified Sampling: The population is divided into subgroups (strata) based on shared characteristics (e.g., age, income). A random sample is taken from each stratum.

2. **Non-Probability Sampling**

In non-probability sampling, not all members of the population have a chance of being included. This approach is faster and cheaper but may introduce bias.