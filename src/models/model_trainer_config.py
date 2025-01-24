from dataclasses import dataclass
import os


@dataclass
class ModelTrainerConfig:
    """
    Configuration class for ModelTrainer.
    Defines paths and directories used during model training and evaluation.
    """

    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")
    catboost_training_dir: str = os.path.join("logs", "catboost_logs")
