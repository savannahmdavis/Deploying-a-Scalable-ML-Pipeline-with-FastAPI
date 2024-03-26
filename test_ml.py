import pytest
from ml.model import train_model, compute_model_metrics
from ml.data import process_data
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd

# TODO: implement the first test. Change the function name and input as needed
def test_model_train_returns_expected():
    """
    Test if the train_model function returns an instance of RandomForestClassifier.
    """
    X_train = np.array([[0, 0], [1, 1]])
    y_train = np.array([0, 0])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model is not RandomForestClassifier."


# TODO: implement the second test. Change the function name and input as needed
def test_process_data_returns_numpy_arrays():
    """
    Test that the process_data function returns features and labels as numpy arrays.
    """
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4],
        'feature2': ['a', 'b', 'a', 'b'],
        'salary': [0, 1, 0, 1]
    })
    cat_features = ['feature2']
    X, y, _, _ = process_data(data, cat_features, label="salary", training=True)
    assert isinstance(X, np.ndarray), "X is not a numpy array."
    assert isinstance(y, np.ndarray), "y is not a numpy array."


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_returns_floats():
    """
    Test that the compute_model_metrics function returns precision, recall, and f1-score as floats.
    """
    y = np.array([0, 1, 0, 1])
    preds = np.array([0, 0, 0, 1])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert all(isinstance(metric, float) for metric in [precision, recall, fbeta]), "Metrics are not all floats."