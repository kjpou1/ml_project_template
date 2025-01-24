import os
from dotenv import load_dotenv
from src.models import SingletonMeta


class Config(metaclass=SingletonMeta):

    _is_initialized = False

    def __init__(self, base_dir=None):
        load_dotenv()  # Load environment variables from .env file
        # Prevent re-initialization
        if not self._is_initialized:
            self.base_dir = base_dir
            # Initialize other configuration settings here
            self._is_initialized = True

    @classmethod
    def initialize(cls):
        # Convenience method to explicitly initialize the Config
        # This method can be expanded to include more initialization parameters if needed
        cls()
