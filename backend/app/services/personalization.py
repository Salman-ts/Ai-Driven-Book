from openai import AsyncOpenAI
from app.core.config import settings
from app.models import UserProfile, Chapter

class PersonalizationService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.model = "gemini-1.5-pro-latest"

    async def personalize_content(
        self, 
        content: str, 
        profile: UserProfile, 
        chapter: Chapter = None
    ) -> str:
        """
        Rewrite content based on user profile (skill, hardware, goals).
        """
        prompt = f"""
        You are an expert educational content adapter.
        
        Learner Profile:
        - Software Skill: {profile.software_skill}
        - Hardware: {profile.hardware_skill}
        - Goal: {profile.learning_goal}
        
        Task:
        Rewrite the following technical content to match the learner's profile.
        - If Beginner: Must simplify complex terms and add analogies.
        - If Expert: Skip basics, focus on implementation and nuance.
        - Use hardware examples relevant to {profile.hardware_skill}.
        
        Original Content:
        {content}
        
        Rewritten Content:
        """
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.choices[0].message.content

personalization_service = PersonalizationService()
