import os

INPUT_PATH = os.getenv("INPUT_PATH")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")


def environments_variables_dict() -> dict:
    return {
        "INPUT_PATH": INPUT_PATH,
        "OUTPUT_PATH": OUTPUT_PATH
    }
