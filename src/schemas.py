from typing import Optional, List
from pydantic import BaseModel, EmailStr
from datetime import date


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: date
    additional_info: Optional[str] = None

class ContactCreate(ContactModel):
    pass

class ContactUpdate(ContactModel):
    pass

class ContactResponse(ContactModel):
    id: int
    owner_id: int

    class Config:
        from_attributes = True


class UserModel(BaseModel):
    email: str
    password: str

class UserDb(BaseModel):
    id: int
    email: str

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"