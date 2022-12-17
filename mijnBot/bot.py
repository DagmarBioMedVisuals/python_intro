import os

import interactions # Python library for Discord interactions
from dotenv import load_dotenv

# import (py) = require (js)

load_dotenv() # laadt de informatie uit .env file

# Setup van Python for Discord library
TOKEN = os.getenv('DISCORD_TOKEN')
client = interactions.Client(token=TOKEN)
GUILD = os.getenv('GUILD_ID')

@client.command(
    name="getstats",
    description="Get your player stats",
    scope=GUILD,
)
async def get_stats(ctx: interactions.CommandContext):
    await ctx.send("Here are your player stats!")

@client.event
async def on_ready(): # Functie bij verbinding bot met server
    print(f'Client has connected to Discord!') # Console log

client.start() # Connect to Discord

# client.stop() # Disconnect the bot

# @client.event
# async def 