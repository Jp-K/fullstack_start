import pyodbc
from sqlalchemy.orm import Session

from config.config import settings


def add_user(db: Session) -> None:

    query = f"""
        INSERT INTO "users" (id, email, hashed_password, is_active)
        VALUES (1, 'joaopaulokraisch@gmail.com', 'slamano', true)
    """

    db.execute(query)
    db.commit()


def init_database(db: Session) -> None:
    add_user(db)