import discord
from discord.ext import commands
import ffmpeg
import DiscordUtils
import youtube_dl
import os
import nacl
import asyncio
import datetime as dt
import random
import typing as t
import json

LYRICS_URL = "https://some-random-api.ml/lyrics?title="
music=DiscordUtils.Music()

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot              
    
    @commands.command(aliases=['play'])
    async def pl(self, ctx,*,url=None):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        
        elif url==None:
            await ctx.send("No URL provided!")
        
        vc=ctx.author.voice.channel
        
        if ctx.voice_client is None:
            await vc.connect()
            ctx.voice_client.stop()
        
        player = music.get_player(guild_id=ctx.guild.id)
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url, search=True)
            song = await player.play()
            await ctx.send(f"Playing {song.name}")
        else:
            song = await player.queue(url, search=True)
            await ctx.send(f"Queued {song.name}")

    @commands.command(aliases=['pause'])
    async def paw(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f"Paused {song.name}")

    @commands.command(aliases=['disconnect'])
    async def dc(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song=await player.stop()
        await ctx.voice_client.disconnect()
    
    @commands.command(alises=['resume'])
    async def res(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f"Resumed {song.name}")

    @commands.command(alises=['stop'])
    async def sp(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song=await player.stop()
        await ctx.send("Stopped playing")

    @commands.command(alises=['loop'])
    async def lp(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            await ctx.send(f"Enabled loop for {song.name}")
        else:
            await ctx.send(f"Disabled loop for {song.name}")

    @commands.command(alises=['now_playing'])
    async def np(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = player.now_playing()
        await ctx.send(song.name)

    @commands.command(alises=['queue'])
    async def q(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")
    
    @commands.command()
    async def skip(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        data = await player.skip(force=True)
        if len(data) == 2:
            await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
        else:
            await ctx.send(f"Skipped {data[0].name}")

    @commands.command(alises=['volume'])
    async def vl(self,ctx,vol):
        player = music.get_player(guild_id=ctx.guild.id)
        song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
        await ctx.send(f"Changed volume for {song.name} to {volume*100}%")

    @commands.command()
    async def rm(ctx, index):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        await ctx.send(f"Removed {song.name} from queue")

    
    

def setup(bot):
    bot.add_cog(Music(bot))