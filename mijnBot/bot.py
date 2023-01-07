import os

import interactions # Python library for Discord interactions
from dotenv import load_dotenv
from spel import Spel
from gevecht import Resultaat

# import (py) = require (js)

load_dotenv() # laadt de informatie uit .env file

# Setup van Python for Discord library
TOKEN = os.getenv('DISCORD_TOKEN')
client = interactions.Client(token=TOKEN)
spel = Spel()
GUILD = os.getenv('GUILD_ID')

@client.command(
    name="getstats",
    description="Get your player stats",
    scope=GUILD,
)
async def get_stats(ctx: interactions.CommandContext):
    speler = spel.get_speler(str(ctx.member.id))
    await ctx.send(f"""{ctx.member.user.username}, hier zijn jouw speler stats:
    
    Attack: {speler.attack}
    HP: {speler.current_hp}
    XP: {speler.xp}
    """)

@client.command(
    name="maakgevecht",
    description="vind een monster om tegen te vechten",
    scope=GUILD
)
async def maak_gevecht(ctx: interactions.CommandContext):
    gevecht = spel.maak_gevecht(str(ctx.member.id))
    await ctx.send(gevecht)

@client.command(
    name="aanval",
    description="val aan!",
    scope=GUILD 
)
async def aanval(ctx: interactions.CommandContext):
    resultaat_bericht = spel.attack(str(ctx.member.id))
    await ctx.send(resultaat_bericht)

@client.event
async def on_ready(): # Functie bij verbinding bot met server
    print(f'Discord bot is online!') # Console log

client.start() # Connect to Discord