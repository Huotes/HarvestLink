# src/main.py

"""Ponto de entrada da aplicação HarvestLink."""

from fastapi import FastAPI
from src.presentation.api.routes import api_router

app = FastAPI(title="HarvestLink")

app.include_router(api_router)
