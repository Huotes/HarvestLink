# src/presentation/api/schemas.py

"""Schemas para validação e serialização dos dados da API."""

from pydantic import BaseModel


class DeviceBase(BaseModel):
    """Dados básicos de um dispositivo."""
    name: str
    status: str
    ip_address: str


class DeviceCreate(DeviceBase):
    """Dados necessários para criação de um dispositivo."""
    pass


class DeviceRead(DeviceBase):
    """Dados retornados ao ler um dispositivo."""
    id: int

    class Config:
        orm_mode = True
