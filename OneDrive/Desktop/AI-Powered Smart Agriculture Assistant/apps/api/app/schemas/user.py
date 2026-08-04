from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    role: Optional[str] = "farmer"

class UserCreate(UserBase):
    clerk_id: str

class User(UserBase):
    id: int
    clerk_id: str
    
    class Config:
        from_attributes = True
