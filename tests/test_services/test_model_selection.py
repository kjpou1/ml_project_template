import os
import pytest
import numpy as np
from sklearn.datasets import make_regression
from sklearn.ensemble import RandomForestRegressor
from src.services.model_selection_service import ModelSelectionService
from src.utils.file_utils import load_object
from src.exception import CustomException


@pytest.fixture
def sample_data():
    """
    Fixture to create sample training and testing data.
    """
    X, y = make_regression(n_samples=100, n_features=5, noise=0.1, random_state=42)
    train_array = np.c_[X[:80], y[:80]]  # 80 samples for training
    test_array = np.c_[X[80:], y[80:]]  # 20 samples for testing
    return train_array, test_array


@pytest.fixture
def model_selection_service(tmp_path):
    """
    Fixture to initialize ModelSelectionService with a temporary model save path.
    """
    service = ModelSelectionService()
    service.model_trainer_config.trained_model_file_path = str(
        tmp_path / "best_model.pkl"
    )
    return service


def test_model_selection_success(sample_data, model_selection_service):
    """
    Test that ModelSelectionService successfully selects and saves the best model.
    """
    train_array, test_array = sample_data
    r2_score = model_selection_service.initiate_model_trainer(train_array, test_array)

    # Assert R2 score is within a reasonable range
    assert r2_score > 0.6, "R2 score is below the acceptable threshold."

    # Verify the best model is saved
    assert os.path.exists(
        model_selection_service.model_trainer_config.trained_model_file_path
    ), "Best model file not found."

    # Verify the saved model is loadable
    best_model = load_object(
        model_selection_service.model_trainer_config.trained_model_file_path
    )
    assert best_model is not None, "Failed to load the best model."


def test_no_model_meets_threshold(sample_data, model_selection_service, monkeypatch):
    """
    Test that ModelSelectionService raises an exception when no model meets the threshold.
    """
    train_array, test_array = sample_data

    # Mock evaluate_models to return low R2 scores
    def mock_evaluate_models(*args, **kwargs):
        return {"Mock Model": 0.5}  # Below threshold

    monkeypatch.setattr(
        "src.services.model_selection_service.evaluate_models", mock_evaluate_models
    )

    with pytest.raises(CustomException) as exc_info:
        model_selection_service.initiate_model_trainer(train_array, test_array)

    assert "No best model found" in str(exc_info.value)


def test_invalid_data_handling(model_selection_service):
    """
    Test that ModelSelectionService raises an exception for invalid input data.
    """
    # Pass invalid data arrays
    invalid_train_array = np.array([[1, 2], [3, 4]])  # Only 2 features
    invalid_test_array = np.array([[5, 6], [7, 8]])  # Only 2 features

    with pytest.raises(CustomException) as exc_info:
        model_selection_service.initiate_model_trainer(
            invalid_train_array, invalid_test_array
        )

    assert "Cannot have number of splits" in str(
        exc_info.value
    ) or "Error in model training" in str(exc_info.value)
