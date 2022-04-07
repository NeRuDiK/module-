# tg: @little_senpai
from .. import loader

class BarsikMod(loader.Module):
	strings = {"name": "Barsik"}
	
	async def client_ready(self, client, db):
		self.client = client
		
	async def watcher(self, message):
		me = (await message.client.get_me())
		client1 = self.client
		result = "Бедный Бусик"
		if message.sender_id != me.id:
			if message.text.lower() == "бб":
				await message.respond(result)
