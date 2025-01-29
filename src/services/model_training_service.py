import logging
import os
import uuid
from datetime import datetime

import numpy as np
from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.config.config import Config
from src.exception import CustomException
from src.models.model_trainer_config import ModelTrainerConfig
from src.utils.file_utils import save_training_artifacts
from src.utils.ml_utils import evaluate_models
from src.utils.yaml_loader import load_model_config


class ModelTrainingService:
    def __init__(self):
        self.config = Config()
        self.logger = logging.getLogger(__name__)
        self.model_trainer_config = ModelTrainerConfig()
        os.makedirs(self.model_trainer_config.catboost_training_dir, exist_ok=True)

    def train_and_validate(
        self, model_name, train_array: np.ndarray, test_array: np.ndarray
    ):
        try:
            # Train the model
            self.logger.info("Starting model training.")

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],  # Features for training
                train_array[:, -1],  # Target for training
                test_array[:, :-1],  # Features for testing
                test_array[:, -1],  # Target for testing
            )

            # # Define models and their hyperparameters
            # models = {
            #     "Random Forest": RandomForestRegressor(),
            #     "Decision Tree": DecisionTreeRegressor(),
            #     "Gradient Boosting": GradientBoostingRegressor(),
            #     "Linear Regression": LinearRegression(),
            #     "XGBRegressor": XGBRegressor(),
            #     "CatBoosting Regressor": CatBoostRegressor(
            #         verbose=False,
            #         train_dir=self.model_trainer_config.catboost_training_dir,
            #     ),
            #     "AdaBoost Regressor": AdaBoostRegressor(),
            # }
            # params = {
            #     "Decision Tree": {
            #         "criterion": [
            #             "squared_error",
            #             "friedman_mse",
            #             "absolute_error",
            #             "poisson",
            #         ],
            #     },
            #     "Random Forest": {
            #         "n_estimators": [8, 16, 32, 64, 128, 256],
            #     },
            #     "Gradient Boosting": {
            #         "learning_rate": [0.1, 0.01, 0.05, 0.001],
            #         "subsample": [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
            #         "n_estimators": [8, 16, 32, 64, 128, 256],
            #     },
            #     "Linear Regression": {},
            #     "XGBRegressor": {
            #         "learning_rate": [0.1, 0.01, 0.05, 0.001],
            #         "n_estimators": [8, 16, 32, 64, 128, 256],
            #         "max_depth": [3, 5, 7],
            #         "subsample": [0.8, 1.0],
            #         "colsample_bytree": [0.8, 1.0],
            #     },
            #     "CatBoosting Regressor": {
            #         "depth": [6, 8, 10],
            #         "learning_rate": [0.01, 0.05, 0.1],
            #         "iterations": [30, 50, 100],
            #     },
            #     "AdaBoost Regressor": {
            #         "learning_rate": [0.1, 0.01, 0.5, 0.001],
            #         "n_estimators": [8, 16, 32, 64, 128, 256],
            #     },
            # }
            model_configs = load_model_config()
            # Initialize models and their parameters
            models = {}
            params = {}

            for model_type, model_info in model_configs["models"].items():
                try:
                    model_class = model_info[
                        "type"
                    ]  # Extract class name (e.g., 'RandomForestRegressor')
                    model_params = model_info.get("params", {})  # Extract parameters

                    # Dynamically instantiate the model using `eval`
                    models[model_type] = eval(model_class)(**model_params)
                    params[model_type] = model_params

                    logging.info(
                        f"Loaded model: {model_name} with params: {model_params}"
                    )
                except Exception as e:
                    logging.error(f"Failed to initialize model {model_type}: {e}")
                    raise CustomException(e)

            # Evaluate all models
            logging.info(
                "Evaluating models with the provided training and testing data."
            )
            # Log the start of evaluation for the current model
            logging.info(f"Evaluating model: {model_name}")
            model = models.get(model_name, {})
            hyper_params = params.get(model_name, {})

            # Perform GridSearchCV if hyperparameters are provided
            if hyper_params:
                gs = GridSearchCV(
                    estimator=model,
                    param_grid=hyper_params,
                    cv=3,
                    scoring="r2",
                    n_jobs=-1,
                    verbose=1,
                )
                gs.fit(X_train, y_train)

                # Update the model with the best parameters
                model.set_params(**gs.best_params_)

            # Train the model
            model.fit(X_train, y_train)

            # Predictions and scoring
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # Log scores for the model
            logging.info(
                f"Model: {model_name} | Train R2: {train_model_score:.4f} | Test R2: {test_model_score:.4f}"
            )

            history = {
                "model": model_name,
                "train_r2": train_model_score,
                "test_r2": test_model_score,
            }

            # Generate metadata and save artifacts
            run_id = (
                datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + str(uuid.uuid4())[:8]
            )

            save_training_artifacts(history, model_name, run_id)

            self.logger.info("Model training completed successfully.")

            return history
        except Exception as e:
            self.logger.error(f"Error during model training: {e}")
            raise
