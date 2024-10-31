import os
from dotenv import load_dotenv

import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main

load_dotenv()

async def main():
    await async_main()
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stoped')