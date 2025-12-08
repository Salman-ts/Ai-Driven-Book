from fastapi import APIRouter, Depends, Body
from app.services.personalization import content_service
from app.services.auth import get_current_user
from pydantic import BaseModel

router = APIRouter()

class ContentRequest(BaseModel):
    content: str

@router.post("/personalize")
async def personalize_chapter(
    request: ContentRequest,
    user: dict = Depends(get_current_user)
):
    # In a real app, fetch profile from DB. Using mock profile from auth/request for now or assume passed.
    # We will assume we fetch the full profile here or the user object has it.
    # For speed, let's mock the profile fetch if not in user dict.
    user_profile = {
        "software_skill": "expert", # TODO: Fetch from DB using user['id']
        "hardware_skill": "raspberry pi",
        "learning_goal": "build a drone"
    }
    
    personalized_content = await content_service.personalize_chapter(request.content, user_profile)
    return {"content": personalized_content}

@router.post("/translate")
async def translate_chapter(
    request: ContentRequest,
    user: dict = Depends(get_current_user)
):
    translated_content = await content_service.translate_to_urdu(request.content)
    return {"content": translated_content}
