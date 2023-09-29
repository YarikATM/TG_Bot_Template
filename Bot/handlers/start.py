from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from Bot.DB.db import Database
from Bot.middlewares.database import DBMiddleware

router = Router()


# router.message.middleware(DBMiddleware(Database))


@router.message(Command("start"))
async def start(message: Message, db: Database):
    res = db.execute_query("SHOW DATABASES")
    await message.answer(
        f"{res}"
    )



