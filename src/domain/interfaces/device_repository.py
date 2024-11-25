# src/domain/interfaces/device_repository.py

"""Interface para o repositório de dispositivos."""

from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.device import Device


class DeviceRepositoryInterface(ABC):
    """Interface que define os métodos do repositório de dispositivos."""

    @abstractmethod
    def add(self, device: Device) -> Device:
        """Adiciona um dispositivo ao repositório."""
        pass

    @abstractmethod
    def get_by_id(self, device_id: int) -> Optional[Device]:
        """Obtém um dispositivo pelo ID."""
        pass

    @abstractmethod
    def update(self, device: Device) -> Device:
        """Atualiza um dispositivo existente."""
        pass

    @abstractmethod
    def delete(self, device_id: int) -> None:
        """Remove um dispositivo pelo ID."""
        pass
