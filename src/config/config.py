import os

from dotenv import load_dotenv

from src.models import SingletonMeta


class Config(metaclass=SingletonMeta):
    """
    Singleton configuration class for managing project-wide constants and directories.
    """

    _is_initialized = False  # Tracks whether the Config has already been initialized

    def __init__(self):
        # Prevent re-initialization
        if Config._is_initialized:
            return

        # Load environment variables
        load_dotenv()

        # Attributes that can be set dynamically
        self._debug = os.getenv("DEBUG", False)
        self._config_path = os.getenv("CONFIG_PATH", "config/default.yaml")

        # Base directory for artifacts
        self.BASE_DIR = os.getenv("BASE_DIR", "artifacts")

        # Subdirectories for artifacts
        self.RAW_DATA_DIR = os.path.join(self.BASE_DIR, "data", "raw")
        self.MODEL_DIR = os.path.join(self.BASE_DIR, "models")
        self.LOG_DIR = os.path.join(self.BASE_DIR, "logs")
        self.HISTORY_DIR = os.path.join(
            self.BASE_DIR, "history"
        )  # Training history directory

        self.REPORTS_DIR = os.path.join(self.BASE_DIR, "reports")
        self.PROCESSED_DATA_DIR = os.path.join(self.BASE_DIR, "data", "processed")

        # Ensure all necessary directories exist
        self._ensure_directories_exist()

        # Mark as initialized
        Config._is_initialized = True

    def _ensure_directories_exist(self):
        """
        Ensures that all necessary directories exist. Creates them if they do not.
        """
        directories = [
            self.RAW_DATA_DIR,
            self.MODEL_DIR,
            self.LOG_DIR,
            self.REPORTS_DIR,
            self.HISTORY_DIR,
        ]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

    @property
    def config_path(self):
        """Get the configuration file path."""
        return self._config_path

    @config_path.setter
    def config_path(self, value):
        """Set the configuration file path."""
        if not isinstance(value, str):
            raise ValueError("config_path must be a string.")
        self._config_path = value

    @property
    def debug(self):
        """Get the debug mode status."""
        return self._debug

    @debug.setter
    def debug(self, value):
        """Set the debug mode status."""
        if not isinstance(value, bool):
            raise ValueError("debug must be a boolean value.")
        self._debug = value

    @classmethod
    def initialize(cls):
        """
        Explicitly initializes the Config singleton.
        This ensures that the configuration is set up before being used in the application.
        """
        if not cls._is_initialized:
            cls()

    @classmethod
    def is_initialized(cls):
        """
        Checks whether the Config singleton has been initialized.
        Returns:
            bool: True if initialized, False otherwise.
        """
        return cls._is_initialized

    @classmethod
    def reset(cls):
        """
        Resets the Config singleton for testing purposes.
        """
        cls._is_initialized = False
        cls._instances = {}
