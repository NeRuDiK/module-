from asyncio import sleep
from .. import loader, utils

def register(cb):
	cb(ЗаёбушкаMod())
	
class ЗаёбушкаMod(loader.Module):
	"""Анти-Зуфар"""
	strings = {'name': 'Анти_Зуфар'}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
		
	async def пиздаcmd(self, message):
		""".пиздец <колличество> <реплай на того, кого заебать>"""
		reply = await message.get_reply_message()
		if not reply:
			await message.edit("<b>Ты криворукий или да?</b>")
			return
		id = reply.sender_id
		args = utils.get_args(message)
		count = 50
		if args:
			if args[0].isdigit():
				if int(args[0]) < 0:
					count = 50
				else:
					count = int(args[0])
		txt = '<a href="tg://user?id={}">{}</a>'
		await message.edit(txt.format(id, "Зуфару пизда"))
		for _ in range(count):
			await sleep(0.5)
			msg = await message.client.send_message(message.to_id, txt.format(id, "Зуфар пидр, нон рут сосо"), reply_to=message)
			if not msg.is_reply:
				await msg.edit("<b>Остановлено!</b>")
				break
			await sleep(0.7)
			await msg.delete()
				
			
