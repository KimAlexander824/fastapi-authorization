from app.core.security import (
    InvalidTokenError,
    create_access_token,
    create_refresh_token,
    decode_access_token,
    verify_password,
)
from app.repositories.users import get_user_by_login
from app.schemas.auth import LoginResponse
from app.schemas.users import UserResponse


class InvalidCredentialsError(Exception):
    pass


def authenticate_user(login: str, password: str) -> LoginResponse:
    user = get_user_by_login(login)
    if user is None or not verify_password(password, user["hashed_password"]):
        raise InvalidCredentialsError

    return LoginResponse(
        access_token=create_access_token(login),
        refresh_token=create_refresh_token(login),
        user=UserResponse.model_validate(user),  # hashed_password отбрасывается схемой
    )


def get_user_by_access_token(token: str) -> UserResponse:
    payload = decode_access_token(token)
    user = get_user_by_login(payload["sub"])
    if user is None:
        raise InvalidTokenError

    return UserResponse.model_validate(user)
