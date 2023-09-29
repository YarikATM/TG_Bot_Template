from typing import Callable, Any, Awaitable
from aiogram import Bot
import aiogram.types
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from Bot.DB.db import Database


class CheckAuth(BaseMiddleware):
    def __init__(self, db, bot):
        self.db: Database = db
        self.bot: Bot = bot

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any]
    ) -> Any:

        user_data: aiogram.types.user.User = data["event_from_user"]
        user_id = user_data.id
        query = 'SELECT user_id FROM Tg_metall.auth_users WHERE user_id = %s'
        res = self.db.execute_query(query, user_id)
        res = bool(len(res))

        if res:
            return await handler(event, data)

        else:
            await self.bot.send_message(user_id, "У вас нет доступа!")
