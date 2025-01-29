from dataclasses import dataclass
from typing import Optional


@dataclass
class CommandLineArgs:
    command: str
    config: str
    debug: bool
