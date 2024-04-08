from aiogram import F, Router
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.orm import Session

from app.crud import CrudUser
from app.models import User
from app.telegram_bot.init import bot

crud_user = CrudUser(User)


class Registration(StatesGroup):
    login_input = State()
    address_input = State()
    address_check = State()
    description_input = State()


router = Router()


@router.message(Command("start"))
async def start(message: Message, state: FSMContext) -> None:
    """
    Adding user into the database after
    user executes /start command.
    """
    await bot.send_message(message.from_user.id, "Привет")