import discord
from discord.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):    
        self.bot=bot
    @commands.command()
    async def usrinfo (self,ctx,mem:discord.Member=None):
        if mem==None:
            embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green(),title='Profile')
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.add_field(name='Name:',value=f"{ctx.author.name}")
            embed.add_field(name="Nickname:",value=f"{ctx.author.display_name}",inline=False)
            embed.add_field(name='Creation date',value=f"{ctx.author.created_at.strftime('%B %d,%Y @ %H:%M %p')} (in UTC)",inline=False)
            embed.add_field(name='Join date',value=f"{ctx.author.joined_at.strftime('%B %d,%Y @ %H:%M %p')} (in UTC)",inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(timestamp=ctx.message.created_at, color=discord.Color.green(),title='Profile')
            embed.set_thumbnail(url=mem.avatar_url)
            embed.add_field(name='Name:',value=f"{mem.name}")
            embed.add_field(name="Nickname:",value=f"{mem.display_name}",inline=False)
            embed.add_field(name='Creation date',value=f"{mem.created_at.strftime('%B %d,%Y @ %H:%M %p')} (in UTC)",inline=False)
            embed.add_field(name='Join date',value=f"{mem.joined_at.strftime('%B %d,%Y @ %H:%M %p')} (in UTC)",inline=False)
            await ctx.send(embed=embed)

    
    @commands.command()
    async def srvinfo (self,ctx):
        embed = discord.Embed(title="Server Information",color= discord.Color.green() )
        name = str(ctx.guild.name)
        owner = str(ctx.guild.owner)
        memberCount = str(ctx.guild.member_count)
        icon = str(ctx.guild.icon_url)
        creation=str(f"{ctx.guild.created_at.strftime('%B %d,%Y @ %H:%M %p')} (in UTC)")
        roles= len(ctx.guild.roles)
        total_text_channels = len(ctx.guild.text_channels)
        total_voice_channels = len(ctx.guild.voice_channels)
        total_channels = total_text_channels  + total_voice_channels 
        
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Name:", value=name, inline=False)
        embed.add_field(name="Owner:", value=owner, inline=False)
        embed.add_field(name="Creation date:", value=creation, inline=False)
        embed.add_field(name="Members:", value=memberCount, inline=False)
        embed.add_field(name="Channels: ", value=total_channels,inline=False )
        embed.add_field(name='Roles:',value=roles,inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def av (self,ctx,mem:discord.Member=None):
        if mem==None:
            mem=ctx.author
            membed=discord.Embed(title=f"{mem.name} 's Avatar")
            membed.set_image(url=mem.avatar_url)
            await ctx.send(embed=membed)
        else:
            membed=discord.Embed(title=f"{mem.name} 's Avatar")
            membed.set_image(url=mem.avatar_url)
            await ctx.send(embed=membed)

    @commands.command()
    async def rl(self,ctx):
        rl=[]
        for r in ctx.guild.roles:
            rl.append(str(r.name))
        rl.pop(0)
        await ctx.send(f"```{rl}```") 
        
def setup(bot):
    bot.add_cog(Info(bot))