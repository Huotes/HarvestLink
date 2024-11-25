#!/bin/bash

# scripts/start.sh

# Ativar ambiente virtual
source venv/bin/activate

# Aplicar migrações do banco de dados
alembic upgrade head

# Iniciar a aplicação
uvicorn src.main:app --host 0.0.0.0 --port 8000
