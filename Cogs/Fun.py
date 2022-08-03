import discord
from discord.ext import commands
import requests
import random
import json

#all functions
def get_quote():
        res1=requests.get('https://zenquotes.io/api/random')   #requesting random quotes from Zenquotes.io
        res1_data= res1.json()[0]
        return f"{res1_data['q']} -{res1_data['a']}"

def cat():
        res2=requests.get('https://api.thecatapi.com/v1/images/search')  #requesting random cat images from thecatapi.com
        return res2.json()[0]['url']

def dog():
        res3=requests.get('https://dog.ceo/api/breeds/image/random')  #requesting random dog images from dog.ceo
        return res3.json()['message']

def shorter(arg):
        res4 = requests.post("https://gotiny.cc/api", json={"input": arg})  #requesting a tiny url for a long url from gotiny.cc
        return res4.json()[0]["code"]

def sun():
    res5=requests.get('https://suntzuapi.herokuapp.com/quote')
    res5_data=res5.json()["quote"]
    return res5_data

#commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.data={}


    @commands.command()
    async def type(self,ctx,arg1=None,*,arg):
        if arg1==None:
            await ctx.send(arg)
        else:
            for i in range (0,int(arg1)):
                await ctx.send(arg)
    
    @commands.command()
    async def quote(self,ctx):
        await ctx.send(get_quote())

    @commands.command()
    async def catto(self,ctx):
        await ctx.send (cat())

    @commands.command()
    async def doggo(self,ctx):
        await ctx.send(dog())

    @commands.command()
    async def short(self,ctx,arg):
        await ctx.send(f'https://gotiny.cc/{shorter(arg)}')

    @commands.command()
    async def randrange(self,ctx,arg,arg1):
        await ctx.send(random.randrange(int(arg),int(arg1)))

    @commands.command()
    async def afk(self,ctx, *, reason=None):
        embed = discord.Embed(timestamp=ctx.message.created_at, color=0x00ffff)
        if reason == None:
            embed.add_field(name=f"{ctx.author.name} is now AFK", value="Reason: No reason specified.")
            embed.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.author.edit(nick=f'{ctx.author.name}[AFK]')
            self.data[ctx.author.id]=reason
            await ctx.send(embed=embed)
            print(self.data)
        else: 
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name=f"{ctx.author.name} is now AFK", value=f"Reason: {reason}", inline=False)
            await ctx.author.edit(nick=f'{ctx.author.name}[AFK]')
            self.data[ctx.author.id]=reason
            await ctx.send(embed=embed)

    @commands.command()
    async def rafk(self,ctx):
        await ctx.author.edit(nick=f'{ctx.author.name}')
        await ctx.send(f'{ctx.author.mention} has returned from being AFK.')
        del self.data[ctx.author.id]


    @commands.Cog.listener()
    async def on_typing(self,channel,user,when):
        if user.id in self.data:
                del self.data[user.id]
                await channel.send(f'<@{user.id}> has returned from being AFK.')
                await user.edit(nick=f'{user.name}')


    @commands.Cog.listener()
    async def on_message(self, message):
        for i in (self.data):
            if (f'<@{self.data[i]}>' in message.content) and not message.author.bot:
                await message.channel.send(f'<@{self.data[i]}> is afk.Reason:{self.data[i]}')
                break

def setup(bot):
    bot.add_cog(Fun(bot))