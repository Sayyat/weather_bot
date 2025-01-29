import datetime

import aiohttp
from aiohttp import ContentTypeError

from config.env import WEATHER_API_KEY


async def get_weather_in(city: str)-> dict:
    async with aiohttp.ClientSession() as session:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(current_date)
        url=f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{current_date}/?key={WEATHER_API_KEY}&unitGroup=metric"
        async with session.get(url) as resp:
            try:
                return await resp.json()
            except ContentTypeError:
                return {}



