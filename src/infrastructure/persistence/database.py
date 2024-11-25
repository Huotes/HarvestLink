# src/infrastructure/persistence/database.py

"""Configuração da conexão com o banco de dados."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from src.config.settings import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db_session():
    """Fornece uma sessão de banco de dados."""
    session = SessionLocal()
    try:
        yield session
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Erro no banco de dados: {e}")
        raise
    finally:
        session.close()
