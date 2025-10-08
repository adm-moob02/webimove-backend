from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from api.core.conf.db import db_settings


Base = declarative_base()


class Database:

    async def get_connstr(self, user: str, passw: str, host: str, port: int, name: str):
        return f"postgresql+asyncpg://{user}:{passw}@{host}:{port}/{name}"

    async def get_engine(self, ):
        configuration = db_settings.model_dump()
        connstr = await self.get_connstr(**configuration)
        return create_async_engine(connstr, echo=True, future=True)

    async def get_db(self, ):
        engine = await self.get_engine()
        Session = sessionmaker(
            bind=engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        async with Session() as session:
            yield session

    async def __call__(self):
        return await self.get_db()


DB = Annotated[Session, Depends(Database)]
