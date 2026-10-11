from pydantic import BaseModel, Field

from app.schemas.users import UserResponse


class LoginRequest(BaseModel):
    login: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=1, max_length=72)


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: UserResponse
