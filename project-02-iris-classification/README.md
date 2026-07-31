# Project 2: Iris Classification (KNN)

A supervised learning model that classifies Iris flowers into 3 species using their sepal and petal measurements.

## What it does

- Loads the Iris dataset (150 samples, 4 features, 3 classes)
- Splits data into training (80%) and test (20%) sets
- Scales features using StandardScaler
- Trains a K-Nearest Neighbors classifier
- Evaluates using confusion matrix and F1 score

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