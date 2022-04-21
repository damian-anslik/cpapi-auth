from datetime import datetime
from urllib3 import disable_warnings
import logging

def configure_logging() -> logging.Logger:
    logging.basicConfig(
        filename=f"logs/log-{datetime.today().date()}.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="a+",
    )
    disable_warnings()
    return logging.getLogger()
