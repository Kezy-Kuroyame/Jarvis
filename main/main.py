import discord
from cfg import discord_cfg
from discord.ext import commands
from discord.utils import get


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='^', intents=intents)


@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен")
    print("---------------")


# @client.event()
# async def hello(ctx):


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


@bot.command(pass_context=True)
async def join(ctx, member: discord.Member):
    print("d")
    channel = ctx.message.author.voice.channel
    print(channel)
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        return await ctx.voice_client.move_to(channel)

    else:
        voice = await channel.connect(reconnect=True, timeout=None)


bot.run(f"{discord_cfg.token}")
