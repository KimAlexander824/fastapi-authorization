from sqlalchemy.orm import Session

from app.core.security import (
    InvalidTokenError,
    create_access_token,
    create_refresh_token,
    decode_access_token,
    verify_password,
)
from app.repositories.users import UserRepository
from app.schemas.auth import LoginResponse
from app.schemas.users import UserResponse


class InvalidCredentialsError(Exception):
    pass


def authenticate_user(session: Session, login: str, password: str) -> LoginResponse:
    user = UserRepository(session).get_by_name(login)
    if user is None or not verify_password(password, user.hashed_password):
        raise InvalidCredentialsError

    return LoginResponse(
        access_token=create_access_token(user.name),
        refresh_token=create_refresh_token(user.name),
        user=UserResponse.model_validate(user),
    )


def get_user_by_access_token(session: Session, token: str) -> UserResponse:
    payload = decode_access_token(token)
    user = UserRepository(session).get_by_name(payload["sub"])
    if user is None:
        raise InvalidTokenError

    return UserResponse.model_validate(user)
