# src/presentation/api/routes.py

"""Definição das rotas da API do HarvestLink."""

from fastapi import APIRouter, Depends
from src.presentation.api.schemas import DeviceCreate, DeviceRead
from src.domain.use_cases.manage_device import ManageDeviceUseCase
from src.infrastructure.repositories.device_repository_impl import DeviceRepositoryImpl
from src.infrastructure.persistence.database import get_db_session

api_router = APIRouter()


@api_router.post('/devices/', response_model=DeviceRead, tags=['Devices'])
def create_device(
    device: DeviceCreate,
    db_session=Depends(get_db_session)
):
    """Endpoint para criar um novo dispositivo."""
    device_repository = DeviceRepositoryImpl(db_session)
    manage_device_use_case = ManageDeviceUseCase(device_repository)
    new_device = manage_device_use_case.register_device(device.dict())
    return new_device


@api_router.get('/devices/{device_id}', response_model=DeviceRead, tags=['Devices'])
def get_device(
    device_id: int,
    db_session=Depends(get_db_session)
):
    """Endpoint para obter informações de um dispositivo específico."""
    device_repository = DeviceRepositoryImpl(db_session)
    manage_device_use_case = ManageDeviceUseCase(device_repository)
    device = manage_device_use_case.get_device(device_id)
    if device:
        return device
    return {'error': 'Device not found'}
