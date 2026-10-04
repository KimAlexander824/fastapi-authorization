from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    login: str = Field(min_length=5)
    password: str = Field(min_length=5)


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
