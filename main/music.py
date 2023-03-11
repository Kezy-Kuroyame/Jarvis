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
            return search_result
        except:
            print("Error downloading")

    async def player(self, ctx):
        voice_client = ctx.voice_client
        while self.songs:
            if voice_client and not voice_client.is_playing():
                song = await self.searching(self.songs[0])
                voice_client.play(discord.FFmpegPCMAudio('tmp/song.mp3'),
                                        after=lambda e: print('Player error: %s' % e) if e else None)
                await asyncio.sleep(song.duration_ms // 1000)
                self.songs.pop(0)

    async def play(self, ctx, *query: str):
        self.songs.append(query)
        if len(self.songs) == 1:
            await self.player(ctx)

    async def clear_queue(self):
        self.songs.clear()

    async def skip(self, ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_connected():
            if self.songs:
                voice_client.stop()
                self.songs.pop(0)
                await self.player(ctx)
            else:
                await ctx.respond("У вас нет песен в очереди")
        else:
            await ctx.respond("Я не подключен к голосовому каналу")

    async def stop(self, ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_connected():
            if voice_client.is_playing():
                print("Stopping..")
                voice_client.stop()
                await self.clear_queue()
                await ctx.respond("Воспроизведение музыки остановлено")
            else:
                print("Error stopping: Бот и так ничего не воспроизводит")
        else:
            print("Error stopping: Бот не находиться в голосовом канале")
            await ctx.respond("Ошибка: У вас ничего не играет")
