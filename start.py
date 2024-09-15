import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


sys.path.append(os.path.dirname(CURRENT_DIR))


os.environ["PYTHONPATH"] = CURRENT_DIR
os.environ["PYTHON_PATH"] = CURRENT_DIR
os.environ["ENVIRONMENT"] = "DEV"
