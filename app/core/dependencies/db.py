from collections.abc import Iterator

from sqlalchemy.orm import Session

from app.db.database import SessionLocal


def get_db() -> Iterator[Session]:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
