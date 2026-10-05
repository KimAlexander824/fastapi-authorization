from fastapi import APIRouter, HTTPException, status

from app.api.decorators import login_required
from app.schemas.auth import LoginRequest, LoginResponse, UserResponse
from app.services.auth import InvalidCredentialsError, authenticate_user

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest) -> LoginResponse:
    try:
        return authenticate_user(data.login, data.password)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
        )


@router.get("/me", response_model=UserResponse)
@login_required
def me(current_user: UserResponse) -> UserResponse:
    return current_user
