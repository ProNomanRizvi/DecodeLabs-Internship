# Project 2: Iris Classification (KNN)

A supervised learning model that classifies Iris flowers into 3 species using their sepal and petal measurements.

## Why this project exists

Project 1 handled fixed, known inputs with hardcoded rules. Real-world data doesn't work that way — it needs a model that can learn patterns from examples and generalize to new, unseen cases. This project builds that fundamental supervised learning pipeline: load data, split it honestly, train a model, and evaluate it properly instead of trusting a single accuracy number.

## What it does

- Loads the Iris dataset (150 samples, 4 features, 3 classes)
- Splits data into training (80%) and test (20%) sets
- Scales features using StandardScaler
- Trains a K-Nearest Neighbors classifier
- Evaluates using confusion matrix and F1 score

## Demo

```
Confusion Matrix:
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]

F1 Score: 1.0000
```

## Files

- `classifier.py` - data loading, training, and evaluation functions
- `tests/test_classifier.py` - automated tests for each pipeline step

## How to run

```bash
python3 classifier.py
```

## How to run tests

```bash
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

## Key concept

Accuracy alone can be misleading, especially on imbalanced data. This project uses a confusion matrix and F1 score to properly evaluate model performance instead of relying on accuracy alone.

## Key decision

The scaler is fit only on the training data, then used to transform the test data separately. Fitting it on the full dataset first would leak information from the test set into training, making the evaluation less honest — even though it's a small detail, it's the difference between a real evaluation and an inflated one.