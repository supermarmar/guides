# **🐍 Python Enhancement Proposals (PEPs)**

<https://peps.python.org/>

<https://medium.com/@opcfrance/python-for-data-engineering-best-practices-a-introductory-guide-d2752f220696>

PEP (Python Enhancement Proposal) documents describe new features, guidelines, or processes for the Python community. Two widely known PEPs are PEP 20 and PEP 8.

## **PEP 8 – Style Guide for Python Code**

- **Indentation and Spacing**: Use 4 spaces per indentation level and avoid mixing tabs and spaces. Keep lines at a maximum of 79 characters.
- **Naming Conventions**:
  - *Variables and functions*: lowercase with underscores (e.g., `train_model`).
  - *Constants*: all uppercase with underscores (e.g., `MAX_ITER`).
  - *Classes*: CamelCase (e.g., `DataFrames`).
- **Imports**: Place imports at the top of the file, grouped as standard libraries, third-party libraries, and local libraries, in that order.

```python
import os
import sys

import numpy as np
import pandas as pd

from src.config import DATA_PATH
```

- **Docstrings and Comments**: Write clear docstrings for classes, methods, and functions. Use comments to explain non-obvious code, especially if it involves complex algorithms or calculations.

## **PEP 20 – The Zen of Python**

```text
Beautiful is better than ugly.

Explicit is better than implicit.

Simple is better than complex.

Complex is better than complicated.

Flat is better than nested.

Sparse is better than dense.

Readability counts.

Special cases aren't special enough to break the rules.

Although practicality beats purity.

Errors should never pass silently.

Unless explicitly silenced.

In the face of ambiguity, refuse the temptation to guess.

There should be one-- and preferably only one --obvious way to do it.

Although that way may not be obvious at first unless you're Dutch.

Now is better than never.

Although never is often better than *right* now.

If the implementation is hard to explain, it's a bad idea.

If the implementation is easy to explain, it may be a good idea.

Namespaces are one honking great idea -- let's do more of those!
```

- **Simplicity and Clarity**: Aim for simple, readable code. Favor readability over complexity, especially in data transformations, feature engineering, and model training steps.
- **Explicitness**: Avoid implicit code structures that might confuse others. For example, when indexing data frames, prefer explicit column names over positions.

## **PEP 257 – Docstring Conventions**

Use clear, concise docstrings for all functions, especially if the code will be used in production or handed off to another team. Follow conventions for one-line and multi-line docstrings, describing the function’s purpose, parameters, and return values.

### Triple-Quoted Strings

This is the most common docstring format in Python. It involves using triple quotes (either single or double) to enclose the documentation text. Triple-quoted strings can span multiple lines and are often placed immediately below the function, class, or module definition.

```python
def my_function():
    '''Demonstrates triple double quotes
    docstrings and does nothing really.'''
 
    return None

print("Using __doc__:")
print(my_function.__doc__)

print("Using help:")
help(my_function)
```

### Google Style Docstrings

Google style docstrings follow a specific format and are inspired by Google's documentation style guide. They provide a structured way to document Python code, including parameters, return values, and descriptions.

```python
def multiply_numbers(a, b):
    """
    Multiplies two numbers and returns the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of a and b.
    """
    return a * b

print(multiply_numbers(3,5))
```

## **PEP 484 – Type Hints**

Type hints make code more readable and help catch errors. They’re especially useful in data pipelines where data types may change.

```python
def add_numbers(x: int, y: int) -> int:
    return x 
```
