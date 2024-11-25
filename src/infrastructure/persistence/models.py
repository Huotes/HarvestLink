# src/infrastructure/persistence/models.py

"""Modelos de banco de dados usando SQLAlchemy."""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.domain.entities.device import Device

Base = declarative_base()


class DeviceModel(Base):
    """Modelo de banco de dados para a entidade Device."""

    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    ip_address = Column(String(45), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def to_entity(self) -> Device:
        """Converte o modelo em uma entidade de domínio."""
        return Device(
            id=self.id,
            name=self.name,
            status=self.status,
            ip_address=self.ip_address
        )

    @staticmethod
    def from_entity(device: Device) -> 'DeviceModel':
        """Cria um modelo a partir de uma entidade de domínio."""
        return DeviceModel(
            id=device.id,
            name=device.name,
            status=device.status,
            ip_address=device.ip_address
        )
