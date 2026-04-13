# **Explaining Models**

Explainable AI (XAI) consists of techniques that help determine how models make decisions. This is especially important in fields like healthcare, finance, and criminal justice, where decisions impact human lives. XAI can help clarify the reasoning behind model predictions, foster trust in the model, and detect biases or errors.

Models can be classified as either black-box or white-box models. Black-box models are complex models whose internal workings aren’t easily understandable. This includes deep neural networks and ensemble models. White-box models, on the other hand, are highly interpretable models whose decision-making process is easily understandable. Examples include linear and logistic regression, decision trees, and other rule-based systems.

Explainability techniques can also be classified into two types: model-agnostic and model-specific.

- Model-specific methods, as the name suggests, are used for specific types of models. These methods use the internal architecture and properties of the model to explain their behavior. Examples include linear and logistic regression coefficients and feature importance in decision trees.
- Model-agnostic methods can be applied to ANY model. This is extremely powerful because they can be used without knowing the type of model or anything about its inner workings. Examples include Permutation Importance, Partial Dependency Plots (PDP), SAPley additive exPlanations (SHAP), and Local Interpretable Model-agnostic Explanations (LIME).
