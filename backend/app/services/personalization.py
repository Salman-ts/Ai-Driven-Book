from openai import AsyncOpenAI
from app.core.config import settings

class ContentService:
    def __init__(self):
        self.openai = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)

    async def personalize_chapter(self, content: str, user_profile: dict) -> str:
        skill = user_profile.get("software_skill", "intermediate")
        hardware = user_profile.get("hardware_skill", "none")
        goal = user_profile.get("learning_goal", "general learning")
        
        prompt = f"""
        You are an expert technical editor. Rewrite the following chapter content to be personalized for a user with these characteristics:
        - Software Skill: {skill}
        - Hardware Interest: {hardware}
        - Learning Goal: {goal}
        
        Instructions:
        1. Adjust the complexity of explanations to match the skill level ({skill}).
        2. If they have hardware interests ({hardware}), add specific examples using that hardware.
        3. relating concepts to their goal: {goal}.
        4. Maintain the core information but make it more engaging for this specific user.
        5. Return ONLY the rewriten markdown.
        
        Original Content:
        {content}
        """
        
        response = await self.openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "system", "content": "You are a helpful educational assistant."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

    async def translate_to_urdu(self, content: str) -> str:
        prompt = f"""
        Translate the following technical content into Urdu.
        
        Requirements:
        1. Use proper Urdu typography and right-to-left formatting logic where applicable (output is markdown).
        2. Keep code blocks in English but translate code comments if possible/appropriate, otherwise keep technical terms in English where standard.
        3. Translate diagram descriptions (alt text).
        4. Output ONLY the translated markdown.
        
        Content:
        {content}
        """
        
        # Using GPT-4 or generic model. Gemini is also requested as option, but OpenAI is configured.
        response = await self.openai.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[{"role": "system", "content": "You are a professional translator expert in Technical Urdu."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

content_service = ContentService()
