from .. import loader, utils
from telethon.tl.types import *
import logging
import io
from telethon.utils import get_display_name

logger = logging.getLogger(__name__)


class PicMod(loader.Module):
    """"Автоматически сохраняет самоуничтожающие фото-видео"""
    strings = {"name": "Pic"}

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client
        self.enable = False

    async def watcher(self, message: Message) -> None:
        if getattr(message, 'media', False) and getattr(message.media, 'ttl_seconds', False) and self.enable:
            media = await self.client.download_media(message.media)
            # media = io.BytesIO(media)
            # media.name = message.file.name or 'unknown'
            name = get_display_name(await self.client.get_entity(message.sender_id))
            logger.info(media)
            return await self.client.send_file("me", media, caption="Self-destructing media from " + name)

    async def piccmd(self, message: Message):
        """Включить/Выключить автоматическое сохранение"""
        if self.enable:
            self.enable = False
            return await utils.answer(message, 'Выключено')
        else:
            self.enable = True
            return await utils.answer(message, 'Включено')
