# from dataclasses import dataclass
# import os


# @dataclass
# class DataIngestionConfig:
#     """
#     Configuration class for data ingestion.
#     Defines the file paths for input data, train data, test data, and raw data.
#     """

#     input_data_path: str = os.path.join(
#         "notebook", "data", "stud.csv"
#     )  # Path to input dataset
#     train_data_path: str = os.path.join(
#         "artifacts", "train.csv"
#     )  # Path to save training data
#     test_data_path: str = os.path.join(
#         "artifacts", "test.csv"
#     )  # Path to save testing data
#     raw_data_path: str = os.path.join(
#         "artifacts", "data.csv"
#     )  # Path to save raw dataset
from dataclasses import dataclass
import os
from src.config.config import Config


@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion.
    Defines the file paths and directories for data ingestion.
    """

    config: Config = Config()  # Access the centralized Config singleton

    # File paths
    input_data_path: str = os.path.join(
        "notebook", "data", "stud.csv"
    )  # Path to input dataset
    train_data_path: str = os.path.join(
        config.PROCESSED_DATA_DIR, "train.csv"
    )  # Training data
    test_data_path: str = os.path.join(
        config.PROCESSED_DATA_DIR, "test.csv"
    )  # Testing data
    raw_data_path: str = os.path.join(config.RAW_DATA_DIR, "data.csv")  # Raw dataset
