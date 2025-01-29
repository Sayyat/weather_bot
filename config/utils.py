from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    commands = [
        BotCommand(command="set_my_city", description="Set my city"),
        BotCommand(command="show_my_city", description="Show my city"),
        BotCommand(command="weather_in_my_city", description="Weather in my city"),
        BotCommand(command="set_language", description="Set language"),
    ]
    await bot.set_my_commands(commands)
