import os
import sys

from src.exception import CustomException
from src.logger_manager import LoggerManager
from src.services.data_ingestion_service import DataIngestionService
from src.services.data_transformation_service import DataTransformationService
from src.services.model_selection_service import ModelSelectionService
from src.utils.file_utils import save_object

logging = LoggerManager.get_logger(__name__)


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_service = DataIngestionService()
        self.data_transformation_service = DataTransformationService()
        self.model_selection_service = ModelSelectionService()

    def run_pipeline(self):
        try:
            # Step 1: Data Ingestion
            logging.info("Starting data ingestion.")
            train_path, test_path = (
                self.data_ingestion_service.initiate_data_ingestion()
            )
            logging.info(f"Data ingested. Train: {train_path}, Test: {test_path}")

            # Step 2: Data Transformation
            logging.info("Starting data transformation.")
            train_arr, test_arr, preprocessor_path = (
                self.data_transformation_service.initiate_data_transformation(
                    train_path, test_path
                )
            )
            logging.info(
                f"Data transformed and preprocessor saved at: {preprocessor_path}"
            )

            # Step 3: Model Training and Selection
            logging.info("Starting model training and selection.")
            results = self.model_selection_service.initiate_model_trainer(
                train_arr, test_arr
            )
            logging.info(f"Model training and selection complete. Results: {results}")

            # Step 4: Save Artifacts
            logging.info("Saving artifacts.")
            # Save the best model
            logging.info("Saving the best model.")
            save_object(
                file_path=self.model_selection_service.model_trainer_config.trained_model_file_path,
                obj=results["best_model"],
            )
            logging.info("Artifacts saved successfully.")
            return results

        except Exception as e:
            logging.error(f"Error in training pipeline: {e}")
            raise CustomException(e, sys) from e
