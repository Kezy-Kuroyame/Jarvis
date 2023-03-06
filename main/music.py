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

    def searching(self, *query):
        search_result = self.client.search(query).best.result
        try:
            search_result.download("tmp/song.mp3", bitrate_in_kbps=320)

        except:
            print("Error downloading")

    async def player(self, ctx):
        voice_client = ctx.voice_client
        self.searching(self.songs[0])
        i = 0
        while i < len(self.songs):
            try:
                voice_client.play(discord.FFmpegPCMAudio('tmp/song.mp3'),
                                  after=lambda e: print('Player error: %s' % e) if e else None)
            except:
                pass
            else:
                self.searching(self.songs[i])
                i += 1

    async def play(self, ctx, *query: str):
        self.songs.append(query)
        if len(self.songs) == 1:
            await self.player(ctx)
