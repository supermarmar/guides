# **Model Classification**

When tackling a problem, you first choose a learning paradigm (supervised, unsupervised, etc.). Then, you select a specific model type. This selection is guided by the nature of your data, the problem you're trying to solve, and the computational resources available.

## **Learning Framework**

This encompasses all approaches to building systems that learn from data. It includes supervised, unsupervised, and reinforcement learning. Within each of these categories, various model types exist. Supervised and unsupervised learning are two fundamental approaches in machine learning, differing primarily in how they use data to train models. Here's a breakdown of their key distinctions:

### **Supervised Learning**

- Data: Uses labelled datasets. This means each data point is tagged with the correct answer or outcome. Think of it like a teacher supervising a student's learning by providing the correct answers to exercises.
- Goal: To learn a mapping between inputs and outputs. The model learns to predict the output for new, unseen inputs based on the patterns it identified in the labelled data.
- Algorithms: Examples include linear regression, logistic regression, support vector machines (SVMs), decision trees, and neural networks.
- Applications:
  - Classification: Predicting categorical outcomes (e.g., spam detection, image recognition).
  - Regression: Predicting continuous values (e.g., house price prediction, stock market forecasting).
- Evaluation: Performance is measured using metrics like accuracy, precision, recall, F1-score, and mean squared error (MSE), depending on the task.

### **Unsupervised Learning**

- Data: Uses unlabelled datasets. The data points have no associated answers or outcomes. The algorithm must discover patterns and structures in the data on its own.
- Goal: To discover hidden patterns, structures, and relationships within the data. The goal isn't to predict a specific outcome, but rather to understand the underlying data structure.
- Algorithms: Examples include k-means clustering, hierarchical clustering, principal component analysis (PCA), and association rule mining.
- Applications:
  - Clustering: Identifying clusters within a dataset like identifying disease outbreak clusters or in natural language processing, in creating word clouds that are semantically related, etc.
  - Dimensionality reduction: They can be used to condense the number of features in a dataset with a high number of features before applying a supervised learning algorithm.
  - Association rule learning: Unsupervised learning algorithms are immensely useful in categorizing uncategorized data and one can then perform the familiar classification/regression tasks using supervised learning.
- Evaluation: More subjective and often relies on visual inspection of results, domain expertise, and metrics like silhouette score for clustering.

## **Parametric Framework**

Parametric models are one category of models within the machine learning framework. They are primarily used in supervised learning (though some applications exist in unsupervised learning). They represent a specific way of learning: by estimating a fixed set of parameters that define the relationship between inputs and outputs.

### **Parametric Models**

Parametric models are best suited for scenarios where the underlying data distribution is well understood, and interpretability is important. These models, such as linear regression or logistic regression, assume a specific functional form and a fixed number of parameters, making them computationally efficient and easy to explain. For instance, credit scoring models in small banks often rely on logistic regression to determine loan approvals, as they provide clear decision rules required for regulatory compliance.

- Assumption: Parametric models assume a specific functional form for the relationship between the dependent and independent variables. This means they assume the data follows a known probability distribution (e.g., normal, exponential, binomial). They have a fixed number of parameters that need to be estimated from the data.
- Estimation: The parameters are estimated using methods like maximum likelihood estimation (MLE) or least squares.
- Advantages:
  - Relatively simple to implement and interpret.
  - Require less data than non-parametric models.
  - Provide concise summaries of the data.
- Disadvantages:
  - Strong assumptions about the data distribution can be violated, leading to biased or inaccurate results if the assumptions are incorrect.
  - May not capture complex relationships in the data.
- Examples: Linear regression, logistic regression, and many generalized linear models (GLMs). These models assume a linear relationship (or a transformation thereof) between the variables.

### **Semi-Parametric Models**

Semi-parametric models, like the Cox Proportional Hazards Model in medical survival analysis, offer a middle ground by making some assumptions while allowing flexibility in certain aspects of the data. This approach is particularly useful when parts of the data structure are unknown or when balancing interpretability with predictive power is necessary. A part of the model is specified parametrically (e.g., the relationship between variables), while another part is left unspecified and estimated non-parametrically (e.g., the distribution of the error term).

- Estimation: Estimation involves a combination of parametric and non-parametric techniques.
- Advantages:
  - More flexible than purely parametric models, allowing for more complex relationships.
  - Less sensitive to violations of distributional assumptions than purely parametric models.
- Disadvantages:
  - Can be more complex to implement and interpret than parametric models.
  - May require more data than parametric models.
- Examples: Partially linear models (combining linear and non-parametric components), Cox proportional hazards model (in survival analysis).

### **Non-Parametric Models**

In contrast, non-parametric models, such as random forests, neural networks, or KNN, are ideal when dealing with large, complex datasets with unknown relationships. These models make fewer assumptions about the data and can capture intricate patterns, making them powerful but less interpretable.They don't assume a specific functional form or probability distribution. For example, fraud detection in banking relies on machine learning algorithms like XGBoost, which can detect anomalies without assuming a predefined relationship between variables. Similarly, deep learning models power recommendation engines on platforms like Netflix and Amazon, where accuracy is prioritized over interpretability. However, the trade-off with non-parametric methods is higher computational cost and potential overfitting, especially with smaller datasets.

- Estimation: Estimation is typically based on local averaging or smoothing techniques.
- Advantages:
  - Very flexible and can capture complex relationships in the data.
  - Robust to violations of distributional assumptions.
- Disadvantages:
  - Require a large amount of data to achieve reliable estimates.
  - Can be more computationally intensive than parametric models.
  - Interpretation can be more challenging.
- Examples: Kernel density estimation, k-nearest neighbours (k-NN), decision trees, support vector machines (SVMs) (depending on the kernel used), and some types of neural networks.
