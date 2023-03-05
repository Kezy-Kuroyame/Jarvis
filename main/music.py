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
        self.client = Client(f'{discord_cfg.yandex_music_token}').init()
        self.client.users_likes_tracks()[0].fetch_track().download('example.mp3')

    async def player(self, voice_client):
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        # song = discord.AudioSource.read('example.mp3')
        voice_client.play(discord.FFmpegPCMAudio(source="https://music.yandex.ru/album/14688437/track/80282466"))

    async def play(self, ctx):
        voice_client = get(self.bot.voice_clients, guild=ctx.guild)
        self.client.users_likes_tracks()[0].fetch_track().download('example.mp3')
        await self.player(voice_client)
