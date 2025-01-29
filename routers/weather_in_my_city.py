from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from services.weather import get_weather_in
from config.i18n import i18n_middleware

_ = i18n_middleware.i18n.gettext

router = Router()


@router.message(Command("weather_in_my_city"))
async def weather_in_my_city_command(message: Message, state: FSMContext):
    state_data = await state.get_data()
    city = state_data.get("my_city")
    if not city:
        await message.answer(_("City is not selected"))
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
