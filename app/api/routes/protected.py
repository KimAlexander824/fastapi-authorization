from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials

from app.api.decorators import bearer_scheme, login_required

router = APIRouter()


# Роутер-пустышка: доступен только с валидным access_token
@router.get("/protected")
@login_required
async def protected(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
):
    return {"message": "You are authorized!"}
