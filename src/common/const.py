# coding: utf-8
from os import makedirs
from os.path import abspath
from pathlib import Path

PROJECT_ROOT = Path(abspath(__file__)).parent.parent.parent
CONF_DIR = PROJECT_ROOT / 'conf'
DATA_DIR = PROJECT_ROOT / 'data'
DB_DIR = PROJECT_ROOT / 'db'
MODEL_DIR = PROJECT_ROOT / 'model'
TEMP_DIR = PROJECT_ROOT / 'temp'

makedirs(CONF_DIR, mode=0o755, exist_ok=True)
makedirs(DATA_DIR, mode=0o755, exist_ok=True)
makedirs(DB_DIR, mode=0o755, exist_ok=True)
makedirs(MODEL_DIR, mode=0o755, exist_ok=True)
makedirs(TEMP_DIR, mode=0o755, exist_ok=True)
