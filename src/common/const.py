# coding: utf-8
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONF_DIR = PROJECT_ROOT / 'conf'
DATA_DIR = PROJECT_ROOT / 'data'
DB_DIR = PROJECT_ROOT / 'db'
MODEL_DIR = PROJECT_ROOT / 'model'
TEMP_DIR = PROJECT_ROOT / 'temp'

DATA_01_RAW = DATA_DIR / '01_raw'
DATA_02_INTERMEDIATE = DATA_DIR / '02_intermediate'
DATA_03_PRIMARY = DATA_DIR / '03_primary'
DATA_04_FEATURE = DATA_DIR / '04_feature'
DATA_05_MODEL_INPUT = DATA_DIR / '05_model_input'
DATA_06_MODELS = DATA_DIR / '06_models'
DATA_07_MODEL_OUTPUT = DATA_DIR / '07_model_output'
DATA_08_REPORTING = DATA_DIR / '08_reporting'
