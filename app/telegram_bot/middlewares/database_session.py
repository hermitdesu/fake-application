from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from app.core.database import db_session_manager


class DatabaseSessionMiddleware(BaseMiddleware):
    """Middleware for passing database session to handlers."""

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        async with db_session_manager() as db:
            data["db"] = db
            return await handler(event, data)
