from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
import re

class UserSignup(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6, description="Password must be at least 6 characters")
    
    # Optional personalization fields
    expertise_level: Optional[str] = Field(default="beginner")
    learning_goal: Optional[str] = Field(default="Learn robotics")
    software_skill: Optional[str] = Field(default="beginner")
    hardware_skill: Optional[str] = Field(default="none")

class UserSignin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
