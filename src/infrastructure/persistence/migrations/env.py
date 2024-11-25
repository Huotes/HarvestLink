# src/infrastructure/persistence/migrations/env.py

"""Arquivo de configuração do Alembic para migrações."""

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))

from src.infrastructure.persistence.models import Base
from src.config.settings import DATABASE_URL

# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)

# Add your model's MetaData object here
target_metadata = Base.metadata

def run_migrations_online():
    """Run migrations in 'online' mode."""
    configuration = context.config.get_section(context.config.config_ini_section)
    configuration['sqlalchemy.url'] = DATABASE_URL
    connectable = engine_from_config(
        configuration,
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
