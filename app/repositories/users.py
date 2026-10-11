from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_name(self, name: str) -> User | None:
        return self.session.scalar(select(User).where(User.name == name))

    def create(self, name: str, hashed_password: str) -> User:
        user = User(name=name, hashed_password=hashed_password)
        self.session.add(user)
        self.session.commit()
        return user
