import os
import sys
import logging
import argparse
from datetime import datetime
from collections import namedtuple


if not os.path.exists('logs'):
    os.mkdir('logs')

LOGGER_FORMAT = (
    "[{levelname:<8}: {name}] - {asctime} : {funcName} @ {lineno:04d}: {msg}"
)

logging.basicConfig(
    format=LOGGER_FORMAT,
    style="{",
    filename=f"logs/log_walkdir_{datetime.today().date().strftime("%d-%m-%Y")}.log",
    level=logging.INFO,
    encoding="utf-8",
    datefmt="%H:%M:%S",
)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(
    logging.Formatter(LOGGER_FORMAT, style="{", datefmt="%d/%m/%Y - %H:%M:%S")
)
LOGGER = logging.getLogger(__name__)
LOGGER.addHandler(stream_handler)

parser = argparse.ArgumentParser(
    description="Программа для сбора иформации о содержимом директории"
)
parser.add_argument("-p", metavar="Path", help="Путь до директории", default=".")
parser.add_argument(
    "-c",
    action="store_true",
    help="Использовать только имя родительской директории вместо полного пути",
)

DirectoryElement = namedtuple(
    "DirectoryElement", ["name", "extension", "is_dir", "root_path"]
)


def get_dir_info(path: str, is_clean: bool) -> list[DirectoryElement]:
    elements = []
    try:
        for root, _, files in os.walk(path):
            LOGGER.info(f"Walked in directory: {root}")

            if root != path:
                root_dirname, dirname = os.path.split(root)

                if is_clean:
                    root_dirname = os.path.split(root_dirname)[1]
                elements.append(DirectoryElement(dirname, None, True, root_dirname))

            for f in files:
                LOGGER.info(f"Found file: {f}")

                if "." in f:
                    filename, extension = f.rsplit(".", 1)
                else:
                    filename, extension = f, ""

                if is_clean:
                    root_path_splitted = root.split("/")

                    if len(root_path_splitted) == 1:
                        root_path_splitted = root_path_splitted[0].split("\\")

                    if root_path_splitted[-1]:
                        root = root_path_splitted[-1]
                    else:
                        root = root_path_splitted[-2]

                elements.append(DirectoryElement(filename, extension, False, root))
        LOGGER.info("Directory walking completed successfully!")
    except KeyboardInterrupt:
        LOGGER.warn("Directory walking has been interrupted!")

    final_string = ",\n\t".join([f"{el}" for el in elements])
    LOGGER.info(f"Final directory elements list: [\n\t{final_string}\n]")

    return elements


if __name__ == "__main__":
    args = parser.parse_args()
    get_dir_info(args.p, args.c)
