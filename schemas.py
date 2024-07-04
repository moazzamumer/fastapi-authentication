from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from passlib.context import CryptContext

# Pydantic schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str


class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    user_id: int
    username: str
    #full_name: Optional[str] = None

    class Config:
        from_attributes = True