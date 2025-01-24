import os
import argparse
from src.models.command_line_args import CommandLineArgs
from .logging_argument_parser import LoggingArgumentParser


class CommandLine:
    @staticmethod
    def parse_arguments() -> CommandLineArgs:
        """
        Parse command-line arguments and return a CommandLineArgs object.
        """
        parser = LoggingArgumentParser(description="Run the application.")

        # Add arguments to the parser
        parser.add_argument(
            "--config", type=str, required=False, help="Path to the configuration file."
        )
        parser.add_argument("--debug", action="store_true", help="Enable debug mode.")
        parser.add_argument(
            "--host",
            type=str,
            default="127.0.0.1",
            help="Specify the host address (default: 127.0.0.1).",
        )

        # Parse the arguments
        args = parser.parse_args()

        # Return a CommandLineArgs object with parsed values
        return CommandLineArgs(config=args.config, debug=args.debug, host=args.host)
