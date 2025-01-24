import os
import sys

import dill  # Serialization library for Python objects
import numpy as np
import pandas as pd

from src.exception import CustomException


def save_object(file_path: str, obj: object) -> None:
    """
    Save a Python object to the specified file path using the `dill` library.

    Args:
        file_path (str): The file path where the object will be saved. If directories in the path do not exist, they will be created.
        obj (object): The Python object to serialize and save.

    Raises:
        CustomException: If an error occurs during the saving process, wraps and raises the error with additional context.

    Example:
        >>> example_obj = {"key": "value"}
        >>> save_object("artifacts/example.pkl", example_obj)
    """
    try:
        # Extract the directory path from the given file path
        dir_path = os.path.dirname(file_path)

        # Ensure the directory exists; create it if it doesn't
        os.makedirs(dir_path, exist_ok=True)

        # Open the file in binary write mode and serialize the object using dill
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        # If an error occurs, raise a CustomException with the error details and system information
        raise CustomException(e, sys) from e


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys) from e
