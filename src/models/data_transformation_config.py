from dataclasses import dataclass
import os


@dataclass
class DataTransformationConfig:
    """
    Configuration for data transformation.
    Defines the file path for saving the preprocessor object.
    """

    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")
