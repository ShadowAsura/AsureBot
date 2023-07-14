import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands

ball8responses = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

load_dotenv()

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Connected to the server")

@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Pong! {latency} ms.")
    
@client.command()
async def commands(ctx):

    await ctx.send("kys")

@client.command(aliases=["8ball", "eightball", "8 ball", "ball 8"])
async def ball8(ctx):
    await ctx.send(ball8responses[random.randint(0, len(ball8responses)-1)])

client.run(os.getenv('TOKEN'))