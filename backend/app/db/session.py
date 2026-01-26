from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# SQLAlchemy Base class for models
Base = declarative_base()

# Convert postgresql:// to postgresql+asyncpg:// for async operations
# The Neon DSN usually comes as postgresql:// but asyncpg requires the driver prefix
db_url = settings.NEON_DSN
if db_url.startswith("postgresql://"):
    db_url = db_url.replace("postgresql://", "postgresql+asyncpg://", 1)
elif db_url.startswith("postgres://"):
    db_url = db_url.replace("postgres://", "postgresql+asyncpg://", 1)

# Create Async Engine
# echo=False to reduce logging noise
engine = create_async_engine(db_url, echo=False)

# Create Session Local
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
