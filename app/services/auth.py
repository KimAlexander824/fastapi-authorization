from app.core.security import create_access_token, create_refresh_token, verify_password
from app.repositories.users import get_user_by_login
from app.schemas.auth import TokenResponse


class InvalidCredentialsError(Exception):
    pass


def authenticate_user(login: str, password: str) -> TokenResponse:
    user = get_user_by_login(login)
    if user is None or not verify_password(password, user["hashed_password"]):
        raise InvalidCredentialsError

    return TokenResponse(
        access_token=create_access_token(login),
        refresh_token=create_refresh_token(login),
    )