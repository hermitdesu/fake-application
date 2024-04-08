import contextlib
from typing import AsyncIterator, Callable

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.core.config import settings


def async_session_factory() -> tuple[
    Callable[[], AsyncIterator[AsyncSession]],
    Callable[[], contextlib.AbstractAsyncContextManager[AsyncSession]],
    AsyncEngine,
]:
    """
    Creating variables to deal with database.

    Returns:
        get_async_db - function to call when creating async db session.
        db_session_manager - function to call when opening db connection in with block.
        db_engine - database sqlalchemy engine.
    """
    async_engine_default_params = {"poolclass": NullPool}

    async_engine = create_async_engine(
        settings.DATABASE_CONNECTIION_URL, **async_engine_default_params
    )
    session_factory = async_sessionmaker(
        bind=async_engine,
        autoflush=False,
        future=True,
        expire_on_commit=False,
    )

    async def get_async_session() -> AsyncIterator[AsyncSession]:
        async with session_factory() as db:
            try:
                yield db
            except Exception as e:
                await db.rollback()
                raise e
            finally:
                await db.commit()
                await db.close()

    return (
        get_async_session,
        contextlib.asynccontextmanager(get_async_session),
        async_engine,
    )


get_db_session, db_session_manager, db_engine = async_session_factory()
