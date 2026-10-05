from pydantic import BaseModel, Field
from app.schemas.users import UserResponse

class LoginRequest(BaseModel):
    login: str = Field(min_length=5)
    password: str = Field(min_length=5)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    user: UserResponse
