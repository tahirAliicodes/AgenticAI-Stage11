# logger.py
# Stage11/logger.py
# Sets up console + file logging for the whole app

import logging
import os
from config import settings

def setup_logger(name: str = "agenticai") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(settings.log_level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    os.makedirs("logs", exist_ok=True)
    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger

logger = setup_logger()