from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.api.routes.protected import router as protected_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(protected_router)
