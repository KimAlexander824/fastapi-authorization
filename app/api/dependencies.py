from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import InvalidTokenError
from app.schemas.users import UserResponse
from app.services.auth import get_user_by_access_token

# Достаёт токен из заголовка "Authorization: Bearer <token>"
# и добавляет кнопку Authorize в Swagger.
# auto_error=False: если заголовка нет, вернёт None, а ошибку отдадим мы сами.
bearer_scheme = HTTPBearer(auto_error=False)


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
