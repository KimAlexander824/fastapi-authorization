from functools import wraps

from fastapi import HTTPException, status
from fastapi.security import HTTPBearer

from app.core.security import InvalidTokenError
from app.services.auth import get_user_by_access_token

bearer_scheme = HTTPBearer(auto_error=False)


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        credentials = kwargs.get("credentials")

        if credentials is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authenticated",
            )

        try:
            get_user_by_access_token(credentials.credentials)
        except InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid or expired token",
            )

        return await func(*args, **kwargs)

    return wrapper
