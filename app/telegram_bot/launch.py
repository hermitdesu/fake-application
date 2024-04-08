"""
Importing all bot functions from files and launching bot.
"""

from app.telegram_bot.client_commands import start
from app.telegram_bot.init import bot, bot_dispatcher
from app.telegram_bot.middlewares import DatabaseSessionMiddleware


async def on_startup() -> None:
    """Info that bot has started"""
    print("Start polling for bot.")


async def run_bot() -> None:
    print("START 1")
    # await bot.delete_webhook(drop_pending_updates=True)
    print("START 2")

    bot_dispatcher.startup.register(on_startup)
    bot_dispatcher.callback_query.outer_middleware(DatabaseSessionMiddleware())
    bot_dispatcher.message.outer_middleware(DatabaseSessionMiddleware())
    bot_dispatcher.include_routers(
        start.router,
    )
    print("START 2")
    await bot_dispatcher.start_polling(bot)
