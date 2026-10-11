from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

password_hash = PasswordHash.recommended()


class InvalidTokenError(Exception):
    pass


def hash_password(plain_password: str) -> str:
    return password_hash.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)


def _create_token(sub: str, token_type: str, expires_delta: timedelta) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def create_access_token(sub: str) -> str:
    return _create_token(sub, "access", timedelta(minutes=settings.access_token_expire_minutes))


def create_refresh_token(sub: str) -> str:
    return _create_token(sub, "refresh", timedelta(days=settings.refresh_token_expire_days))


def decode_token(token: str, expected_type: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
            options={"require": ["sub", "type", "exp"]},
        )
    except jwt.InvalidTokenError as error:
        raise InvalidTokenError from error

    if payload["type"] != expected_type:
        raise InvalidTokenError

    return payload


def decode_access_token(token: str) -> dict:
    return decode_token(token, "access")
