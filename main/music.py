import asyncio
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
    def __init__(self, bot):
        self.bot = bot
        self.client = Client(f'{discord_cfg.yandex_music_token}').init()
        self.songs = []

    async def searching(self, *query):
        search_result = self.client.search(query).best.result
        try:
            search_result.download("tmp/song.mp3", bitrate_in_kbps=320)
        except:
            print("Error downloading")

    async def player(self, ctx):
        voice_client = ctx.voice_client
        while self.songs:
            await self.searching(self.songs[0])
            try:
                voice_client.play(discord.FFmpegPCMAudio('tmp/song.mp3'),
                                  after=lambda e: print('Player error: %s' % e) if e else None)
            except:
                pass
            else:
                self.songs.pop(0)

    async def play(self, ctx, *query: str):
        self.songs.append(query)
        if len(self.songs) == 1:
            await self.player(ctx)

    async def clear_queue(self):
        self.songs.clear()

    async def stop(self, ctx):
        voice_client = ctx.voice_client

