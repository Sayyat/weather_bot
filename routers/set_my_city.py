from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message


router = Router()

from config.i18n import i18n_middleware
_ = i18n_middleware.i18n.gettext


class SetMyCityGroup(StatesGroup):
    set_my_city = State()

@router.message(Command("set_my_city"))
async def set_my_city_command(message: Message, state: FSMContext):
    await state.set_state(SetMyCityGroup.set_my_city)
    await message.answer(_("Write your city"))

@router.message(SetMyCityGroup.set_my_city)
async def set_my_city_handler(message: Message, state: FSMContext):
    await state.update_data(my_city=message.text)
    await state.set_state(None)
    await message.answer(_("Your city changed to {text}").format(text=message.text))