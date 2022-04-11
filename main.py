import os, discord, time, random, asyncio
import time
import asyncio
from dotenv import load_dotenv
from keep_alive import keep_alive
from discord.ext import commands
client = commands.Bot(command_prefix="!", self_bot=True, help_command=None)
clown= 1

token= "your token"


@client.event
async def on_ready():
 while clown < 2:
   channel = client.get_channel(959451848018886747)
   await channel.send('!water')
   time.sleep(61)

#made by u/kerem_akti58 or rick sanches#0024 in discord
keep_alive()
client.run(token, bot=False)