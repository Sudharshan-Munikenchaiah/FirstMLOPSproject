import os
from pathlib import Path
import logging

list_of_files=[
    ".github\\workflow\\.gitkeep",
    "src\\__init__.py",
    "src\\components\\__init__.py",
    "src\\components\\data_ingestion.py",
    "src\\components\\data_transformation.py",
    "src\\components\\model_trainer.py",
    "src\\components\\model_evaluation.py",
    "src\\pipeline\\__init__.py",
    "src\\pipeline\\training_pipeline.py",
    "src\\pipeline\\prediction_pipeline.py",
    "src\\utils\\__init__.py",
    "src\\utils\\util.py",
    "src\\logger\\logging.py",
    "src\\exception\\exception",
    "test\\unit\\__init__.py",
    "test\\integration\\__init__.py",
    "init_setup.sh",
    "Requirements.txt",
    "Requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment\experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating a directory {filedir} for {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass


print("Hello world")
