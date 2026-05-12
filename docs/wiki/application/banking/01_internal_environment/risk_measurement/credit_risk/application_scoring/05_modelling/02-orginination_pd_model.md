---
tags:
  - application/banking/internal-environment/risk-measurement/credit-risk/application-scorecards/modelling/orginination-pd-model
  - difficulty/unknown
  - study-status/new
aliases:
---
# Origination PD

## **Logistic Regression**

Logistic regression is a commonly used statistical technique in credit risk modeling due to its simplicity, interpretability, and effectiveness in binary classification problems, such as determining whether a borrower will default (1) or not default (0) on a loan. The model estimates a score (between 0 and 1) that represents the likelihood of default based on borrower characteristics and financial behavior.

Logistic regression models the relationship between a set of independent variables (e.g., income, credit history length) and a binary [[wiki/application/banking/01_internal_environment/risk_measurement/credit_risk/a-irb_capital/04_feature_engineering/pd/01-target_variable|target variable]] (default or no default) by applying a **logistic (sigmoid) function** to a linear equation. Provides a continuous risk score rather than a binary result, enabling nuanced decisions (e.g., risk-based pricing). Easy to implement and explain to stakeholders. You can decide to build different models for different segmentations.

The model creates a linear equation: 

$z=\alpha + \Beta_1 X_1 + \Beta_2 X_2 + ... + \Beta_n X_n$
- $\Beta_i$ are the coefficients (weights) learned during model training.
- $X_i$ are the independent variables (features).

The logistic regression model transforms $z$ into a probability using the sigmoid function

$p=P(y=1)=\frac{1}{1+e^{-z}}$

By default, a threshold (e.g., 0.5) is applied to classify outcomes. If $p>0.5$ then $y=1$ else $y=0$.

**Loss Function**: The model minimizes the log-loss or negative log-likelihood, which measures the difference between predicted probabilities and actual outcomes.

**Limitations**: Logistic regression assumes a linear relationship between features and the log-odds of default, which might not always hold. If defaults are rare (imbalanced dataset), the model may perform poorly without adjustments (e.g., oversampling or weighting).

## **XGBoost**

XGBoost (Extreme Gradient Boosting) is a high-performance, scalable machine learning algorithm often used in credit risk modeling for its ability to handle complex, non-linear relationships between variables. XGBoost excels in capturing complex patterns and interactions in the data, making it particularly effective for high-dimensional or non-linear datasets.

**Ensemble Learning**: XGBoost is an ensemble learning technique based on gradient boosting, which builds a series of decision trees sequentially to minimize the prediction error. XGBoost combines multiple weak learners (decision trees) into a strong learner. Each tree focuses on correcting the errors made by the previous trees. At each step, XGBoost uses the gradient (first derivative of the loss function) and the Hessian (second derivative) to optimize predictions.

- First Tree: Predicts initial probabilities (e.g., default rate = 10% across the dataset). Splits data to minimize error (e.g., splits on "Credit History Length").
- Residual Calculation: Computes residuals (difference between actual and predicted probabilities).
- Second Tree: Focuses on residuals and further refines predictions by splitting on another feature (e.g., "Income").
- Final Prediction: Combine the outputs of all trees to get a probability score for default.

**Benefits**: Unlike logistic regression, XGBoost can model complex, non-linear interactions between features. It can make some incorrect inferences so you have to do some spot checks e.g. Actuary vs Nurse and their PDs. It identifies the most important variables contributing to predictions (feature importance).

**Limitations**: XGBoost models are harder to interpret than logistic regression, though feature importance and SHAP values can help. More computationally intensive, especially for large datasets. Requires careful tuning (e.g., learning rate, number of trees, max depth) to achieve optimal performance.