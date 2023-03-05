import os
import requests
from bs4 import BeautifulSoup
from yandex_music import Client
from yandex_music.exceptions import YandexMusicError
from yandex_music.utils.request import Request

from cfg import discord_cfg
from discord.utils import get
import discord


class Music:
    songs = []

    def __init__(self, bot):
        self.bot = bot




    async def player(self, voice_client, songs, ctx):
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        voice_client.play(discord.FFmpegPCMAudio(f"{songs}", **ffmpeg_options))

    async def play(self, ctx):
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        self.client.users_likes_tracks()[0].fetch_track().download('example.mp3')
        # await self.player(voice_client, 'example.mp3', ctx)
