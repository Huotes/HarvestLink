# src/shared/utils.py

"""Funções utilitárias compartilhadas pelo aplicativo."""

import hashlib


def hash_text(text: str) -> str:
    """Gera um hash SHA256 de uma string."""
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
