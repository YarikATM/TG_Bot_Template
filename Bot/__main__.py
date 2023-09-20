import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config.config_reader import config
from aiogram import F


# from handlers import admin


def setup_logging() -> None:
    logging.basicConfig(level=logging.DEBUG)


def setup_handlers(dp: Dispatcher) -> None:
    # dp.include_router(admin.router)
    pass


async def setup_aiogram(dp: Dispatcher) -> None:
    logging.debug("Configuring aiogram")
    # create db connection
    setup_handlers(dp)
    # setup_middlewares(dp)
    logging.info("Configured aiogram")


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(dispatcher)


def main() -> None:
    setup_logging()

    if config.DEBUG:
        bot_token = config.DEBUG_BOT_TOKEN
    else:
        bot_token = config.BOT_TOKEN

    bot = Bot(token=bot_token.get_secret_value(), parse_mode="HTML")

    dp = Dispatcher(
        # storage=SystemStorage
    )

    # start polling
    dp.startup.register(aiogram_on_startup_polling)
    asyncio.run(dp.start_polling(bot))


if __name__ == '__main__':
    main()
