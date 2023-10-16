import speechkit
import discord
from cfg import discord_cfg
from discord.ext import commands
from discord.utils import get
from discord import Option
import asyncio

from main.music import Music
# from voice_recording import start_record, stop_recording

intents = discord.Intents.all()
intents.message_content = True
# intents.message_content = True
# intents.presences = True
# intents.members = True

bot = commands.Bot(
    command_prefix="/",
    intents=intents
)
music = Music(bot)


@bot.slash_command(name='record', description='Manually records audio', guild_ids=[872819304754724884])
# # async def manual_record(ctx):
#     await ctx.defer()
#     await start_record(ctx)
#     await asyncio.sleep(4)
#     await stop_recording(ctx)



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


@bot.slash_command(name="join", guild_ids=[872819304754724884])
async def join(ctx):
    channel = ctx.author.voice.channel
    voice_client = ctx.voice_client
    # await ctx.delete()
    print(channel)

    if voice_client and voice_client.is_connected():
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()
        await music.clear_queue()


@bot.slash_command(name="play", guild_ids=[872819304754724884])
async def play(ctx, query: Option(str, description="Название песни", required=True)):
    await join(ctx)

    await music.play(ctx, query)


@bot.slash_command(name="stop", guild_ids=[872819304754724884])
async def stop(ctx):
    await music.stop(ctx)


@bot.slash_command(name="skip", guild_ids=[872819304754724884])
async def skip(ctx):
    await music.skip(ctx)

bot.run(f"{discord_cfg.token}")
