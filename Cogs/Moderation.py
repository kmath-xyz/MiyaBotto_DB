import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,arg=5):
        await ctx.channel.purge(limit=arg+1)
        await ctx.send(f'Cleared {arg} messages')
        await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.has_permissions(kick_members=True,ban_members=True)
    async def kick(self,ctx, mem : discord.Member,*,reason=None):
        await mem.kick(reason=reason)
        await ctx.send(f'User {mem.mention} has been kicked.\nReason: {reason}.')

    @commands.command()
    @commands.has_permissions(kick_members=True,ban_members=True)
    async def ban(self,ctx, mem : discord.Member,*,reason=None):
        await mem.ban(reason=reason)
        await ctx.send(f'User {mem.mention} has been banned. \nReason: {reason}.')

    @commands.command()
    @commands.has_permissions(kick_members=True,ban_members=True)
    async def mute(self,ctx, mem : discord.Member,*,reason=None):
        guild = ctx.guild
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await mem.add_roles(mute_role)
        await ctx.send(f'User {mem.mention} has been muted. \nReason: {reason}.')

    @commands.command()
    @commands.has_permissions(kick_members=True,ban_members=True)
    async def unmute(self,ctx, mem : discord.Member,*,reason=None):
        guild = ctx.guild
        mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
        await mem.remove_roles(mute_role)
        await ctx.send(f'User {mem.mention} has been unmuted. \nReason: {reason}.')

    @commands.command()
    @commands.has_permissions(kick_members=True, ban_members=True)
    async def w(self,ctx, mem : discord.Member,*,reason=None):
        await ctx.send(f'User {mem.mention} has been warned. \nReason: {reason}.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ar (self,ctx,arg,mem:discord.Member):
        guild = ctx.guild
        role = discord.utils.get(ctx.guild.roles, name=f'{arg}')
        await mem.add_roles(role)
        await ctx.send(f'User {mem.mention} has been given the role "{role}".')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rr (self,ctx,arg,mem:discord.Member):
        guild = ctx.guild
        role = discord.utils.get(ctx.guild.roles, name=f'{arg}')
        await mem.remove_roles(role)
        await ctx.send(f'The role "{role}" has been taken away from {mem.mention}.')



def setup(bot):
    bot.add_cog(Moderation(bot))


