# tests/test_classifier.py
# Tests for the Iris classification pipeline

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from classifier import load_data, prepare_data, train_model, evaluate_model


def test_load_data_shape():
    # Iris has 150 samples, 4 features, and 150 matching labels
    X, y = load_data()
    assert X.shape == (150, 4)
    assert y.shape == (150,)


def test_prepare_data_split_size():
    # 20% test size on 150 samples should give 30 test samples, 120 train
    X, y = load_data()
    X_train, X_test, y_train, y_test = prepare_data(X, y)
    assert len(X_train) == 120
    assert len(X_test) == 30


def test_train_model_returns_fitted_model():
    # Model should be able to predict after training, without errors
    X, y = load_data()
    X_train, X_test, y_train, y_test = prepare_data(X, y)
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    assert len(predictions) == len(y_test)


def test_evaluate_model_f1_score_range():
    # F1 score must always be between 0 and 1
    X, y = load_data()
    X_train, X_test, y_train, y_test = prepare_data(X, y)
    model = train_model(X_train, y_train)
    matrix, f1 = evaluate_model(model, X_test, y_test)
    assert 0.0 <= f1 <= 1.0


def test_evaluate_model_confusion_matrix_shape():
    # 3 classes means a 3x3 confusion matrix
    X, y = load_data()
    X_train, X_test, y_train, y_test = prepare_data(X, y)
    model = train_model(X_train, y_train)
    matrix, f1 = evaluate_model(model, X_test, y_test)
    assert matrix.shape == (3, 3)