from fastapi import APIRouter, HTTPException, status

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth import InvalidCredentialsError, authenticate_user

router = APIRouter()


@router.post("/me", response_model=TokenResponse)
def login(data: LoginRequest) -> TokenResponse:
    try:
        return authenticate_user(data.login, data.password)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login or password",
        )