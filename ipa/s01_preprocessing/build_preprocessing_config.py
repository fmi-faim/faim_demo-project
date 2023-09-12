"""
build_preprocessing_config.py
=============================

Ask for user input via command line interface (CLI) to build the
preprocessing_config.yaml. The preprocessing_config.yaml is consumed
by the run_preprocessing.py script.
"""


import os
import questionary
import yaml

CONFIG_NAME = "preprocessing_config.yaml"


def main() -> None:
    """
    Create preprocessing_config.yaml from user inputs.
    """
    cwd = os.getcwd()

    raw_data_dir = questionary.path("Path to raw data directory:").ask()
    output_dir = questionary.path("Path to output directory:").ask()

    output_dir = os.path.join(output_dir, "01_preprocessing")

    config = {
        "raw_data_dir": os.path.relpath(raw_data_dir, cwd),
        "output_dir": os.path.relpath(output_dir, cwd),
    }

    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(cwd, CONFIG_NAME), "w") as f:
        yaml.safe_dump(config, f)


if __name__ == "__main__":
    main()
