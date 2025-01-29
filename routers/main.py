from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from config.bot import bot
from config.i18n import i18n_middleware
from config.utils import set_bot_commands
from services.weather import get_weather_in

router = Router()

_ = i18n_middleware.i18n.gettext


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    user_name = message.from_user.full_name
    await message.answer(
        _("Hi {user_name}, this is Weather bot, you can now the weather in any city by writing me weather:your_city").format(
            user_name=user_name)
    )
    # await set_bot_commands(bot)


@router.message(F.text.startswith("weather:"))
async def weather_input_command(message: Message, state: FSMContext):
    __, city = message.text.split(":")

    if not city or len(city.strip()) == 0:
        await message.answer("City not selected")
        return

    weather = await get_weather_in(city)
    current_conditions = weather.get("currentConditions", {})
    text = _("Weather data for {city}:\n"
             "Temperature: {temp}\n"
             "Feels like: {feelslike}\n"
             "Humidity: {humidity}\n"
             "Sunrise: {sunrise}\n"
             "Sunset: {sunset}\n").format(
        city=city,
        temp=current_conditions.get("temp", 0),
        feelslike=current_conditions.get("feelslike", 0),
        humidity=current_conditions.get("humidity", 0),
        sunrise=current_conditions.get("sunrise", 0),
        sunset=current_conditions.get("sunset", 0),
    )
    await message.answer(text)
