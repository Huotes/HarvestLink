# src/infrastructure/repositories/device_repository_impl.py

"""Implementação do repositório de dispositivos usando SQLAlchemy."""

from typing import Optional
from sqlalchemy.orm import Session
from src.domain.entities.device import Device
from src.domain.interfaces.device_repository import DeviceRepositoryInterface
from src.infrastructure.persistence.models import DeviceModel


class DeviceRepositoryImpl(DeviceRepositoryInterface):
    """Repositório de dispositivos usando SQLAlchemy."""

    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def add(self, device: Device) -> Device:
        """Adiciona um dispositivo ao banco de dados."""
        device_model = DeviceModel.from_entity(device)
        self.db_session.add(device_model)
        self.db_session.commit()
        self.db_session.refresh(device_model)
        return device_model.to_entity()

    def get_by_id(self, device_id: int) -> Optional[Device]:
        """Obtém um dispositivo pelo ID."""
        device_model = self.db_session.query(DeviceModel).filter_by(id=device_id).first()
        if device_model:
            return device_model.to_entity()
        return None

    def update(self, device: Device) -> Device:
        """Atualiza um dispositivo existente."""
        device_model = self.db_session.query(DeviceModel).filter_by(id=device.id).first()
        if device_model:
            device_model.name = device.name
            device_model.status = device.status
            device_model.ip_address = device.ip_address
            self.db_session.commit()
            return device_model.to_entity()
        return None

    def delete(self, device_id: int) -> None:
        """Remove um dispositivo pelo ID."""
        device_model = self.db_session.query(DeviceModel).filter_by(id=device_id).first()
        if device_model:
            self.db_session.delete(device_model)
            self.db_session.commit()
