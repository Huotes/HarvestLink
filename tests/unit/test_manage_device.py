# tests/unit/test_manage_device.py

"""Testes unitários para o caso de uso ManageDeviceUseCase."""

import unittest
from unittest.mock import MagicMock
from src.domain.use_cases.manage_device import ManageDeviceUseCase
from src.domain.entities.device import Device


class TestManageDeviceUseCase(unittest.TestCase):
    """Classe de testes para ManageDeviceUseCase."""

    def setUp(self):
        self.device_repository = MagicMock()
        self.manage_device_use_case = ManageDeviceUseCase(self.device_repository)

    def test_register_device(self):
        """Teste para o método register_device."""
        device_data = {
            'id': 1,
            'name': 'Device 1',
            'status': 'active',
            'ip_address': '192.168.0.1'
        }
        device = Device(**device_data)
        self.device_repository.add.return_value = device

        result = self.manage_device_use_case.register_device(device_data)

        self.device_repository.add.assert_called_once()
        self.assertEqual(result, device)

    def test_get_device(self):
        """Teste para o método get_device."""
        device = Device(id=1, name='Device 1', status='active', ip_address='192.168.0.1')
        self.device_repository.get_by_id.return_value = device

        result = self.manage_device_use_case.get_device(1)

        self.device_repository.get_by_id.assert_called_once_with(1)
        self.assertEqual(result, device)


if __name__ == '__main__':
    unittest.main()
