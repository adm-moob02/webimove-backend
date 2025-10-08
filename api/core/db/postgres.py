from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from api.core.conf.db import db_settings


Base = declarative_base()


async def get_connstr(user: str, passw: str, host: str, port: int, name: str):
    return f"postgresql+asyncpg://{user}:{passw}@{host}:{port}/{name}"


async def get_engine():
    configuration = db_settings.model_dump()
    connstr = await get_connstr(**configuration)
    return create_async_engine(connstr, echo=True, future=True)


async def get_db():
    engine = await get_engine()
    Session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with Session() as session:
        yield session


DB = Annotated[Session, Depends(get_db)]
