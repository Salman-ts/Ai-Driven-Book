from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI
from app.core.config import settings

router = APIRouter()

# Initialize Gemini client
client = AsyncOpenAI(
    api_key=settings.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

class ContentRequest(BaseModel):
    content: str

@router.post("/personalize")
async def personalize_chapter(request: ContentRequest):
    """
    Personalize chapter content for the user's skill level.
    Temporarily without auth for easier testing.
    """
    try:
        prompt = f"""You are an expert educational content adapter.
        
Learner Profile:
- Software Skill: Intermediate
- Hardware: Simulation Only
- Goal: Learn robotics fundamentals

Task:
Rewrite the following technical content to be more engaging and easier to understand.
Add helpful analogies and practical examples where useful.

Original Content:
{request.content[:3000]}

Rewritten Content:
"""
        
        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        
        return {"personalized_content": response.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Personalization error: {str(e)}")


@router.post("/translate")
async def translate_chapter(request: ContentRequest):
    """
    Translate chapter content to Urdu.
    """
    try:
        prompt = f"""You are an expert translator specializing in technical content.

Translate the following robotics educational content to Urdu.
Keep technical terms in English but explain them in Urdu context.
Maintain the educational and engaging tone.

Original (English):
{request.content[:3000]}

Urdu Translation:
"""
        
        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        
        return {"translated_content": response.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")


@router.get("/health")
async def content_health():
    """Health check for content service."""
    return {"status": "healthy", "service": "content"}
