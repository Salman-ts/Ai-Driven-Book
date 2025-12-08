from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.future import select
from app.db.session import get_db
from app.db.models import User, UserProfile
from app.services.auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

router = APIRouter()

class ProfileUpdate(BaseModel):
    software_skill: str
    hardware_skill: str
    learning_goal: str

@router.post("/profile")
async def update_profile(
    profile_data: ProfileUpdate,
    user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Check if user exists in our DB, if not create
    result = await db.execute(select(User).where(User.id == user["id"]))
    db_user = result.scalars().first()
    
    if not db_user:
        db_user = User(id=user["id"], name=user["name"], email=f"{user['id']}@example.com") # Mock email if not provided
        db.add(db_user)
        await db.flush()
        
    # Update or Create Profile
    result = await db.execute(select(UserProfile).where(UserProfile.user_id == user["id"]))
    db_profile = result.scalars().first()
    
    if not db_profile:
        db_profile = UserProfile(user_id=user["id"])
        db.add(db_profile)
    
    db_profile.software_skill = profile_data.software_skill
    db_profile.hardware_skill = profile_data.hardware_skill
    db_profile.learning_goal = profile_data.learning_goal
    
    await db.commit()
    return {"status": "updated"}

@router.get("/me")
async def get_my_profile(
    user: dict = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(User).where(User.id == user["id"]))
    db_user = result.scalars().first()
    
    if not db_user:
        return {"user": user, "profile": None, "points": 0}
        
    # Get Profile
    profile_result = await db.execute(select(UserProfile).where(UserProfile.user_id == user["id"]))
    db_profile = profile_result.scalars().first()
    
    # Calculate Points (Mock logic or sum logs)
    # points = ...
    
    return {
        "user": user,
        "profile": {
            "software_skill": db_profile.software_skill if db_profile else None,
            "hardware_skill": db_profile.hardware_skill if db_profile else None
        },
        "points": 100 # Base points
    }
