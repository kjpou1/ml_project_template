from dataclasses import dataclass
import os


@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion.
    Defines the file paths for input data, train data, test data, and raw data.
    """

    input_data_path: str = os.path.join(
        "notebook", "data", "stud.csv"
    )  # Path to input dataset
    train_data_path: str = os.path.join(
        "artifacts", "train.csv"
    )  # Path to save training data
    test_data_path: str = os.path.join(
        "artifacts", "test.csv"
    )  # Path to save testing data
    raw_data_path: str = os.path.join(
        "artifacts", "data.csv"
    )  # Path to save raw dataset
