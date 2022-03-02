import discord
from discord.ext import commands, tasks

token = ""
bot = commands.Bot()

@bot.event
async def on_ready():
    print(bot.user.name + "\'s online")

bot.run(token) 
