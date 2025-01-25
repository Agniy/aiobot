from pathlib import Path
from dataclasses import dataclass
from typing import Final

@dataclass
class Settings:
    # Base directories
    ROOT_DIR: Final[Path] = Path(__file__).parent.parent
    HANDLERS_DIR: Final[Path] = ROOT_DIR / "handlers"
    LOGS_DIR: Final[Path] = ROOT_DIR / "logs"
    STATIC_DIR: Final[Path] = ROOT_DIR / "static"

    # Files
    LOG_FILE: Final[Path] = LOGS_DIR / "bot_logs.log"
    ENV_FILE: Final[Path] = ROOT_DIR / ".env"

    # Create required directories
    def create_directories(self) -> None:
        self.LOGS_DIR.mkdir(exist_ok=True)
        self.STATIC_DIR.mkdir(exist_ok=True)

# Create singleton instance
settings = Settings()
