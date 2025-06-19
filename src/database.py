from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


# Database setup (Async SQLAlchemy)
DATABASE_URL = "sqlite+aiosqlite:///./db.sqlite3"
engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# Database session dependency
async def async_get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session