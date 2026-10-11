"""
Создаёт таблицы в SQLite и добавляет пользователя.

Запуск из корня проекта:
    python -m scripts.create_user
    python -m scripts.create_user --name alice --password secret
"""
import argparse

import app.models  # noqa: F401  регистрирует модели в Base.metadata
from app.core.security import hash_password
from app.db.database import Base, SessionLocal, engine
from app.repositories.users import UserRepository


def main() -> None:
    parser = argparse.ArgumentParser(description="Создать пользователя в базе")
    parser.add_argument("--name", default="johndoe")
    parser.add_argument("--password", default="12345")
    args = parser.parse_args()

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as session:
        users = UserRepository(session)
        if users.get_by_name(args.name) is not None:
            print(f"Пользователь '{args.name}' уже существует")
            return

        user = users.create(args.name, hash_password(args.password))
        print(f"Создан пользователь id={user.id}, name='{user.name}'")


if __name__ == "__main__":
    main()
