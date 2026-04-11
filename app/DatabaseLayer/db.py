from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

try:
    DATABASE_URL = os.getenv("DATABASE_URL")
except Exception as e:
    print(f"Error loading environment variables: {e}")
    raise
# For High performance 👇
# engine = create_async_engine(
#     DATABASE_URL,
#     echo=False,              # 🔥 disable in prod
#     future=True,
#     pool_size=10,            # 🔥 tune this
#     max_overflow=20,         # 🔥 handle spikes
#     pool_timeout=30,
#     pool_recycle=1800,
#     pool_pre_ping=True       # 🔥 avoid stale connections
# )
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # no logging overhead
    pool_pre_ping=True   # avoids stale connection issues
)
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() :
    async with async_session() as session:
        yield session