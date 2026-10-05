from fastapi import APIRouter

from app.api.decorators import login_required

router = APIRouter()


# Роутер-пустышка: доступен только с валидным access_token
@router.get("/protected")
@login_required
def protected():
    return {"message": "You are authorized!"}
