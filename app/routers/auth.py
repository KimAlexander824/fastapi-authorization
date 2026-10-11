from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies.auth import get_current_user
from app.core.dependencies.db import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.schemas.users import UserResponse
from app.services.auth import InvalidCredentialsError, authenticate_user

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)) -> LoginResponse:
    try:
        return authenticate_user(db, data.login, data.password)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
        )


@router.get("/me", response_model=UserResponse)
def me(current_user: UserResponse = Depends(get_current_user)) -> UserResponse:
    return current_user
