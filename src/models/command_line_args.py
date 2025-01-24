from dataclasses import dataclass


@dataclass
class CommandLineArgs:
    config: str
    debug: bool
    host: str = "127.0.0.1"  # Default value for host
