from datetime import datetime, timedelta, timezone
from pwdlib import PasswordHash
from app.core.config import settings
import jwt

password_hash = PasswordHash.recommended()  # создаёт объект с рекомендуемым алгоритмом хеширования паролей (обычно Argon2).


def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


def create_token(sub: str, token_type: str, expires_delta: timedelta):
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)


def create_access_token(sub: str):
    return create_token(sub, "access", timedelta(minutes=settings.access_token_expire_minutes))


def create_refresh_token(sub: str):
    return create_token(sub, "refresh", timedelta(days=settings.refresh_token_expire_days))
