import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "base-project-fastapi"
    PROJECT_VERSION: str = "0.0.0"

    BASE_DIR = Path(__file__).resolve().parent.parent
