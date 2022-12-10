import os

import interactions # Python library for Discord interactions
from dotenv import load_dotenv

# import (py) = require (js)

load_dotenv() # laadt de informatie uit .env file

# Setup van Python for Discord library
TOKEN = os.getenv('DISCORD_TOKEN')
client = interactions.Client(token=TOKEN)

@client.event
async def on_ready(): # Functie bij verbinding bot met server
    print(f'Client has connected to Discord!') # Console log

client.start() # Connect to Discord

# client.stop() # Disconnect the bot

# @client.event
# async def 