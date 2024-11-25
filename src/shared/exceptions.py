# src/shared/exceptions.py

"""Definição de exceções personalizadas para o HarvestLink."""


class HarvestLinkException(Exception):
    """Exceção base para o HarvestLink."""
    pass


class DeviceNotFoundException(HarvestLinkException):
    """Exceção lançada quando um dispositivo não é encontrado."""
    pass


class DatabaseException(HarvestLinkException):
    """Exceção para erros relacionados ao banco de dados."""
    pass
