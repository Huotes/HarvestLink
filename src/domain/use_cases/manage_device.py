# src/domain/use_cases/manage_device.py

"""Caso de uso para gerenciamento de dispositivos."""

from src.domain.entities.device import Device
from src.domain.interfaces.device_repository import DeviceRepositoryInterface


class ManageDeviceUseCase:
    """Classe responsável por gerenciar dispositivos."""

    def __init__(self, device_repository: DeviceRepositoryInterface) -> None:
        self.device_repository = device_repository

    def register_device(self, device_data: dict) -> Device:
        """Registra um novo dispositivo."""
        device = Device(**device_data)
        return self.device_repository.add(device)

    def get_device(self, device_id: int) -> Device:
        """Obtém um dispositivo pelo ID."""
        return self.device_repository.get_by_id(device_id)

    def update_device(self, device_id: int, device_data: dict) -> Device:
        """Atualiza um dispositivo existente."""
        device = self.device_repository.get_by_id(device_id)
        if device:
            for key, value in device_data.items():
                setattr(device, key, value)
            return self.device_repository.update(device)
        return None

    def delete_device(self, device_id: int) -> None:
        """Remove um dispositivo."""
        self.device_repository.delete(device_id)
