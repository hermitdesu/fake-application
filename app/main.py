import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

import asyncio

from app import telegram_bot

if __name__ == "__main__":
    asyncio.run(telegram_bot.run_bot())
