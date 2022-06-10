from .. import loader, utils
from telethon.tl.types import Message
import logging
from random import choice

logger = logging.getLogger(__name__)


@loader.tds
class AnimatedQuotesMod(loader.Module):
    """Простой модуль для создания анимированные стикеров. \n [tg: @little_senpai]"""

    strings = {
        "name": "AnimatedQuotes",
        "no_text": "🚫 <b>Ой, ошибочка вышла</b>",
        "processing": "<b>Ща всё будет...</b>",
    }

    async def client_ready(self, client, db) -> None:
        self._client = client

    async def aniqcmd(self, message: Message) -> None:
        """<Ваш текст> - Анимированный стикер"""
        args = utils.get_args_raw(message)
        if not args:
            await utils.answer(message, self.strings("no_text"))
            return

        message = await utils.answer(message, self.strings("processing"))
        if isinstance(message, (list, set, tuple)):
            message = message[0]

        try:
            query = await self._client.inline_query("@QuotAfBot", args)
            await message.respond(file=choice(query).document)
        except Exception as e:
            await utils.answer(message, str(e))
            return

        await message.delete()