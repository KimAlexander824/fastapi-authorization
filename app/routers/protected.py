from fastapi import APIRouter, Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.decorators.auth import login_required
from app.core.dependencies.auth import bearer_scheme
from app.core.dependencies.db import get_db

router = APIRouter()


@router.get("/protected")
@login_required
async def protected(
        credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
        db: Session = Depends(get_db),
):
    return {"message": "You are authorized!"}
