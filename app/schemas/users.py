from pydantic import BaseModel


class UserResponse(BaseModel):
    username: str
    full_name: str
    email: str
