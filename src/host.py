import asyncio
from src.config.config import Config
from src.models.command_line_args import CommandLineArgs
from src.logger_manager import LoggerManager
from src.services.data_ingestion_service import DataIngestionService
from src.services.data_transformation_service import DataTransformationService
from src.services.model_selection_service import ModelSelectionService
from src.logger_manager import LoggerManager

logging = LoggerManager.get_logger(__name__)


class Host:
    """
    Host class to manage the execution of the main application.

    This class handles initialization with command-line arguments and
    configuration, and runs the main asynchronous functionality.
    """

    def __init__(self, args: CommandLineArgs):
        """
        Initialize the Host class with command-line arguments and configuration.

        Parameters:
        args (CommandLineArgs): Command-line arguments passed to the script.
        """
        self.args = args
        self.config = Config()
        logging.info("Host initialized with arguments: %s", self.args)

    def run(self):
        """
        Synchronously run the asynchronous run_async method.

        This is a blocking call that wraps the asynchronous method.
        """
        return asyncio.run(self.run_async())

    async def run_async(self):
        """
        Main asynchronous method to execute the host functionality.

        Logs the start and end of the execution and can be extended
        to perform additional tasks.
        """
        try:
            logging.info("Starting host operations.")
            # Placeholder for asynchronous tasks (e.g., service calls, workflows)
            # await some_async_task()

            # Perform data ingestion
            data_ingestion = DataIngestionService()
            train_data, test_data = data_ingestion.initiate_data_ingestion()

            # Perform data transformation
            data_transformation = DataTransformationService()
            train_arr, test_arr, preprocessor_path = (
                data_transformation.initiate_data_transformation(train_data, test_data)
            )

            logging.info("Data ingestion and transformation completed.")
            logging.info(f"Preprocessor saved at: {preprocessor_path}")

            model_trainer = ModelSelectionService()
            model_trainer.initiate_model_trainer(
                train_array=train_arr, test_array=test_arr
            )

            logging.info("Host operations completed successfully.")
        except Exception as e:
            logging.error("An error occurred during host operations: %s", e)
        finally:
            logging.info("Shutting down host gracefully.")
