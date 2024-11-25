# config/settings.py

"""Configurações globais da aplicação HarvestLink."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/harvestlink_db')

SECRET_KEY = os.getenv('SECRET_KEY', 'sua_chave_secreta')
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
