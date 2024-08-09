import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage,Redis
import asyncio
from handlers import router

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s - [%(pathname)s:%(lineno)d]',
    handlers=[
        logging.StreamHandler()
    ]
)
logging.captureWarnings(False)

async def main():
    try:
        bot = Bot(os.getenv("BOT_TOKEN"))
        redis = Redis(host=os.getenv('REDIS_HOST','localhost'), port=6379, db=0, password=os.getenv('REDIS_PASSWORD'),decode_responses=True)
        redis_storage=RedisStorage(redis=redis)
        dp = Dispatcher(storage=redis_storage)
        dp.include_router(router)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"ERROR MAIN \n\n\nALARM\n\n\n {e}")


if __name__ == '__main__':
    asyncio.run(main())
