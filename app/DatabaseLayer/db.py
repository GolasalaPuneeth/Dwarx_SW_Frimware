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

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() :
    async with async_session() as session:
        yield session