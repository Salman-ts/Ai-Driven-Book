from sqlalchemy.future import select
from app.db.session import AsyncSessionLocal
from app.db.models import PointLog, User

async def award_points(user_id: str, points: int, reason: str):
    async with AsyncSessionLocal() as session:
        # Verify user exists
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalars().first()
        if not user:
            # Create user stub if not exists (should handle in auth, but safety net)
            pass
            
        log = PointLog(user_id=user_id, points=points, reason=reason)
        session.add(log)
        await session.commit()
        return log.points
