import discord
from cfg import discord_cfg


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("MTA4MTU1MDk5MDcxODgwNDA0MA.GLT3YW.M62WL4DtAgjETPSZwU-6cWLqTttv91Ed2LjExg")
