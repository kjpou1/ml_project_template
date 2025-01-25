import asyncio
from src.models.command_line_args import CommandLineArgs
from src.logger_manager import LoggerManager
from src.pipeline.train_pipeline import TrainPipeline
from src.exception import CustomException

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

        Leverages the TrainPipeline to perform data ingestion, transformation,
        and model training in a centralized and structured manner.
        """
        try:
            logging.info("Starting host operations.")

            # Initialize and execute the training pipeline
            train_pipeline = TrainPipeline()
            result = train_pipeline.run_pipeline()

            # Log the results from the pipeline
            logging.info("Pipeline execution completed successfully.")
            logging.info("Results: %s", result)

        except CustomException as e:
            logging.error("A custom error occurred during host operations: %s", e)
            raise  # Re-raise to handle further if needed
        except Exception as e:
            logging.error("An unexpected error occurred: %s", e)
            raise  # Re-raise to ensure visibility of unexpected errors
        finally:
            logging.info("Shutting down host gracefully.")
