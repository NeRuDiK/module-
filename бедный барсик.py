from .. import loader

class аfkMod(loader.Module):
	strings = {"name": "аfk"}
	
	async def client_ready(self, client, db):
		self.client = client
		
	async def watcher(self, message):
		me = (await message.client.get_me())
		client1 = self.client
		result = "бедный барсик"
		if message.sender_id != me.id:
			if message.text.lower() == "бб":
				await message.respond(result)