#all modules
import discord
from discord.ext import commands
import os
import DiscordUtils
from config import *
intents = discord.Intents.default()
intents.members = True
botto=commands.Bot(command_prefix='.',intents=intents)
botto.remove_command('help')


#events:

@botto.event
async def on_ready():
    print('We have logged in as {0.user}'.format(botto))
    await botto.change_presence(activity=discord.Game('.help'), status=discord.Status.online)

#On joining

@botto.event
async def on_member_join(member):
    await (member.guild.system_channel).send(f"Welcome! {member.mention} We hope you enjoy your stay at {member.guild.name}.\n Member count={member.guild.member_count}")


#On leaving

@botto.event
async def on_member_remove(member):
   await (member.guild.system_channel).send(f"{member.mention} has left the server.") 

for fn in os.listdir('./Cogs'):
    if fn.endswith('.py'):
        botto.load_extension(f'Cogs.{fn[:-3]}')

P1=discord.Embed(color= discord.Color.green())
P1.add_field(name="Fun commands:", value='**AFK:** Sets AFK for the user.\n \n **Catto:** Shows a random cat image.\n \n **Doggo:** Sends a random dog image.\n \n **Quote:** Sends a random quote. \n \n **Rafk:** Used to remove AFK. \n\n **Randrange**: Takes a range of numbers and sends a random no. \n \n**Short:** Accepts a long URL and returns a short URL.\n\n **Type:** Accepts a number and sentence, and then repeats the sentence the same number of times. [Ex: .type 5 Hello.]\n \n```Following commands need to be executed in lower case.```', inline=False)


P2=discord.Embed(color= discord.Color.green())
P2.add_field(name="Music commands:", value="**Pl:** Plays songs.[Ex: .pl (URL) or .pl (Song name)].\n \n **Paw:** Pauses a song.\n \n **Res:** Resume the song.\n \n **Np:** Shows the current song that's playing.\n \n **Lp:** Loops or Unloops the song. \n \n **Q:** Shows the queue. \n\n **Rm:** Removes the given song from the queue.\n\n **Skip**: Skips the current song. \n\n **Sp:** Stops playing the song and clears the queue.\n\n **Vl:** Adjusts the volume.\n \n **Dc:** Disconnects the bot from VC.\n \n```Following commands need to be executed in lower case.```",inline=False)

P3=discord.Embed(color= discord.Color.green())
P3.add_field(name="Info", value="**Av:** Shows the avatar of the given user or the sender if no user's given.\n \n **Srvinfo:** Shows server info.\n \n **Usrinfo:** Shows the info about a user.\n \n **Rl:** Shows the list of roles in the server.\n \n ```Following commands need to be executed in lower case.```",inline=False)

P4=discord.Embed(color= discord.Color.green())
P4.add_field(name="Moderation", value="**Kick:** Kicks the user from the server.\n \n **Ban:** Bans the user from the server.\n \n **Clear:** Clears messages. [Ex: .clear 10 (Default=5)]\n \n **Mute:** Mutes a user. (The mute role should already exist.)\n \n **Unmute:** Unmutes the user.\n \n **W:** Warns a user.\n \n **Ar:** Gives the specified role to the user. [Ex: .ar test @User].\n \n **Rr:** Takes away the specified role from the user.\n \n ```Following commands need to be executed in lower case.```",inline=False)
    
@botto.command()
async def help(ctx):
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('▶️', "next")
    embeds = [P1,P2,P3,P4,P1]
    await paginator.run(embeds)


botto.run(token)

