from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncSession
from src.config import config

engine = AsyncEngine(
    create_engine(
url=config.DATABASE_URL,
    echo=True,
))