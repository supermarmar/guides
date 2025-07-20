# **Hyperparameters**

A hyperparameter of a machine learning model is a value that determines part of the learning process and is not affected by training unlike a parameter, which is learned during the model training process. You’re probably already familiar with some hyperparameters. Let’s look at some examples.

In the k-nearest neighbors algorithm, k is a hyperparameter. k determines how many neighbors will be used, and training data does not change k.

Decision trees also use hyperparameters. Before training a decision tree classifier, you might want to specify how deep the tree can go (i.e., how many splits are allowed before arriving at a leaf). You might also want to specify the minimum number of samples that are present in a node in order to split that node. Both of those values are hyperparameters. They determine the structure of the model, but they are not learned during training.

Regularization factors are another example. In linear or logistic regression, regularization is a term that is added to the loss function in order to penalize models with large coefficients. The coefficients are the parameters of the model here! The regularization factor is a hyperparameter. The value of the regularization factor affects how large the coefficients of a regression model will be, but the regularization factor is independent of training data.

## **Hyperparameter Tuning**

Hyperparameters can make or break a machine learning model. Take the k-nearest neighbors algorithm as an example. Recall that in k-nn classification, the class of a sample is determined by the classes of its k nearest neighbors from the training data. If k is too large, classes with a small number of samples might be missed, and the model could underfit the data. If k is too small, it’s possible that outliers in the training data could misclassify their neighbors. The model could be overfit to those outliers.

This balance between overfitting and underfitting is called the bias-variance tradeoff. It’s an important consideration for supervised machine learning.

- Bias is the difference between a model’s predictions and the correct values. Models with a lot of bias underfit the data and will perform poorly on both testing and training data. In biased models, the structure of the model overpowers the training data.
- Variance refers to the dependence of a model on training data. A model has high variance if different training data results in widely varying outcomes. This often leads to overfitting a model to training data. Overfit, high-variance models generally perform well on training data, but poorly on testing data. In this case, the training data overpowers the structure of the model.

The bias variance tradeoff is called a tradeoff because decreasing the bias usually increases the variance. The converse is also true: decreasing variance usually increases the bias. Good machine learning models strike a balance. We can reduce bias by making a model more sensitive to training data, but we do so at the risk of overfitting. On the other hand, we can reduce variance by restricting a model so that it is less affected by training data. This, however, runs the risk of underfitting the model.

Ultimately, we want models that perform well on testing data. One way to do that is to choose the right hyperparameters. In the case of supervised machine learning, we want hyperparameters that make a good compromise between bias and variance. This can be done by training a model multiple times, each time with different hyperparameter values, and then using the best ones. This process is called hyperparameter tuning. There are several different ways of doing this.
When tuning hyperparameters, it’s important to split the data into training, testing, and validation data. Training data is used to train the model. Validation data is used to evaluate hyperparameters. After a hyperparameter is tuned, the model can be tested on testing data. This data allows for an estimate of model performance that isn’t affected by the hyperparameter tuning process.
Here’s a table that lists several machine learning algorithms, some of their hyperparameters, and possible tuning methods. This table is not exhaustive: some machine learning algorithms have many hyperparameters that aren’t listed here. If you want to learn more about the hyperparameters for a specific model in scikit-learn, the documentation is a good place to start.

| ML Algorithm | scikit-learn package | Hyperparameters | Parameters in sklearn | Notes | How to tune |
|---------------------------------|----------------------------------------------------|------------------------------------------------------|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Linear Regression with gradient descent | `sklearn.linear_model.SGDRegressor` | Learning rate, regularization penalty | `learning_rate`, `penalty`, `alpha` | Set `penalty` to 11 or 12 (default). `alpha` is the regularization strength. Larger `alpha` will result in stronger regularization. | `learning_rate` and `C` can be tuned with a grid search or random search. |
| Logistic regression | `sklearn.linear_model.LogisticRegression` | Regularization penalty | `penalty`, `C` | Set `penalty` to 11, 12 (default), or `None`. `C` is the inverse of regularization strength. Smaller `C` will result in stronger regularization. | `C` can be tuned with a grid search or random search. |
| k-nearest neighbors | `sklearn.neighbors.KNeighborsClassifier` | k (the number of neighbors) | `n_neighbors` | | `n_neighbors` can be tuned with a grid search or random search. |
| Decision trees | `sklearn.tree.DecisionTreeClassifier` | Maximum depth of the tree, minimum number of samples to split an internal node | `max_depth`, `min_samples_split` | | `max_depth` and `min_samples_split` can be tuned with a grid search or random search. |
| k-means | `sklearn.cluster.KMeans` | k (the number of clusters) | `n_clusters` | Use the elbow method. | |
| Support vector machines | `sklearn.svm.SVC` | Regularization penalty | `C` | Smaller `C` will result in stronger regularization. | `C` can be tuned with a grid search or random search. |
