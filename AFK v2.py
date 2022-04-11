# tg: @little_senpai
import time
from datetime import datetime

from telethon import types

from .. import loader, utils


@loader.tds
class AFKMod(loader.Module):
	"""Выводит сообщение о том, что вы не в сети"""
	strings = {"name": "AFK",
	           "gone": "<b>Я ушёл в AFK</b>",
	           "back": "<b>Я больше не в AFK</b>",
	           "afk": "<b>Я сейчас не в сети\n(Был в сети {} назад).</b>",
	           "afk_reason": "<b>Я сейчас не в сети\n(Был в сети {} назад).\nПричина:</b> <i>{}</i>"}

	def __init__(self):
		self.config = loader.ModuleConfig(
			"EXCEPTION_ID", [""], "Exceptions users IDs")

	async def client_ready(self, client, db):
		self._db = db
		self._me = await client.get_me()

	async def afkcmd(self, message):
		""".afk [Напишите сообщение - почему не в сети]"""
		if utils.get_args_raw(message):
			self._db.set(__name__, "afk", utils.get_args_raw(message))
		else:
			self._db.set(__name__, "afk", True)
		self._db.set(__name__, "gone", time.time())
		await self.allmodules.log(".afk", data=utils.get_args_raw(message) or None)
		await utils.answer(message, self.strings("gone", message))

	async def unafkcmd(self, message):
		"""Выключить AFK статус"""
		self._db.set(__name__, "afk", False)
		self._db.set(__name__, "gone", None)
		await self.allmodules.log(".unafk")
		await utils.answer(message, self.strings("back", message))

	async def watcher(self, message):
		if not self.get_afk():
			return
		if str(message.sender_id) in self.config["EXCEPTION_ID"]:
			return
		if not isinstance(message, types.Message):
			return
		now = datetime.now().replace(microsecond=0)
		gone = datetime.fromtimestamp(self._db.get(__name__, "gone")).replace(microsecond=0)
		diff = now - gone
		if getattr(message.to_id, "user_id", None) == self._me.id:
			if not self.get_afk():
				return
			afk_state = self.get_afk()
			ret = self.strings("afk_reason", message).format(diff, afk_state)
			await utils.answer(message, ret)
		elif message.mentioned:
			if self.get_afk():
				afk_state = self.get_afk()
				ret = self.strings("afk_reason", message).format(diff, afk_state)
				await utils.answer(message, ret, reply_to=message)
			else:
				return

	def get_afk(self):
		return self._db.get(__name__, "afk", False)
