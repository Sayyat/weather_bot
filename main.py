import asyncio
import logging
import sys

from aiogram import Dispatcher

from config.i18n import i18n_middleware
from routers.main import router as main_router
from routers.set_my_city import router as set_my_city_router
from routers.set_language import router as set_language_router
from routers.show_my_city import router as show_my_city_router
from routers.weather_in_my_city import router as weather_in_my_city_router
from config.bot import bot

dp = Dispatcher()
dp.update.middleware(i18n_middleware)

async def main():
    dp.include_routers(
        main_router,
        set_language_router,
        set_my_city_router,
        show_my_city_router,
        weather_in_my_city_router
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
