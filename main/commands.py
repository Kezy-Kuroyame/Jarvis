import discord
from cfg import discord_cfg
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
# import voice_recording


intents = discord.Intents.all()
intents.message_content = True
# intents.message_content = True
# intents.presences = True
# intents.members = True

bot = commands.Bot(
    command_prefix="/",
    intents=intents
)


@bot.slash_command(name='record', description='Manually records audio', guild_ids=[872819304754724884])
async def manual_record(ctx):
    await ctx.defer()
    await start_record(ctx)
    asyncio.sleep(5)
    await stop_recording(ctx)


@bot.slash_command(name='hehe', guild_ids=[872819304754724884])
async def hello(ctx):
    await ctx.delete()
    """Adds two numbers together."""
    await ctx.send("Пососи")


@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен")
    print("---------------")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello!')


@bot.slash_command(name="join",  guild_ids=[872819304754724884])
async def join(ctx):
    print("d")
    channel = ctx.author.voice.channel
    print(channel)
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        return await ctx.voice_client.move_to(channel)

    else:
        await channel.connect()


bot.run(f"{discord_cfg.token}")
