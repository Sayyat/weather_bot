from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config.i18n import i18n_middleware
_ = i18n_middleware.i18n.gettext


router = Router()


@router.message(Command("show_my_city"))
async def show_my_city_command(message: Message, state: FSMContext):
    state_data = await state.get_data()
    city = state_data.get("my_city")
    await message.answer(_("Your city: {city}").format(city=city))

