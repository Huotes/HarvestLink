# src/domain/entities/device.py

"""Entidade Device representando um dispositivo no domínio do HarvestLink."""

from dataclasses import dataclass


@dataclass
class Device:
    """Classe que representa um dispositivo."""
    id: int
    name: str
    status: str
    ip_address: str
