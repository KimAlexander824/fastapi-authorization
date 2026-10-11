from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.dependencies.db import get_db
from app.core.security import InvalidTokenError
from app.schemas.users import UserResponse
from app.services.auth import get_user_by_access_token

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
        credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
        db: Session = Depends(get_db),
) -> UserResponse:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authenticated",
        )

    try:
        return get_user_by_access_token(db, credentials.credentials)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid or expired token",
        )
