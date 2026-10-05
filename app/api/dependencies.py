from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials

from app.api.decorators import bearer_scheme
from app.core.security import InvalidTokenError
from app.schemas.users import UserResponse
from app.services.auth import get_user_by_access_token


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> UserResponse:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authenticated",
        )

    try:
        return get_user_by_access_token(credentials.credentials)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or expired token",
        )