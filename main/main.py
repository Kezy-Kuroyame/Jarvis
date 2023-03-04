import discord
from cfg import discord_cfg
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='//', intents=intents)


@client.event
async def on_ready():
    print(f"Бот {client.user} запущен")
    print("---------------")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


@bot.command()
async def join(ctx, member: discord.Member):
    channel = ctx.message.author.voice.channel
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    print(channel)
    await channel.connect(reconnect=True, timeout=None)


client.run(f"{discord_cfg.token}")
