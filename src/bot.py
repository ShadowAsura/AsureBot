import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix="*", intents=discord.intents.all())

@client.event
async def on_ready():
    print("Connected to the server")

client.run(os.getenv('TOKEN'))