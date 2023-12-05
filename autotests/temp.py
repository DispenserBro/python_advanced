import logging
from datetime import datetime
import sys

LOGGER_FORMAT = "[{levelname:<8}: {name}] - {asctime} : {funcName} @ {lineno:04d}: {msg}"
logging.basicConfig(
    format=LOGGER_FORMAT,
    style="{",
    filename=f"logs/log_{datetime.today().date().strftime("%d-%m-%Y")}.log",
    level=logging.INFO,
    encoding="utf-8",
    datefmt="%H:%M:%S"
)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter(LOGGER_FORMAT, style="{", datefmt="%d/%m/%Y - %H:%M:%S"))
logger = logging.getLogger(__name__)
logger.addHandler(stream_handler)


def main():
    logger.warning("Incorrect data!")
    logger.critical("Failed to write data!")
    logger.info("Exiting...")
    


if __name__ == "__main__":
    logger.info("Starting...")
    main()
