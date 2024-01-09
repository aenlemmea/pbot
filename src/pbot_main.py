import disnake
from disnake.ext import commands
import os
import asyncio
from disnake.ext import commands
from datetime import datetime
from dotenv import load_dotenv
from handlers.gfg_scrap import getUpcomingContestListgfg

load_dotenv()
discord_token = os.getenv('discord_token')

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) 

async def showContestListgfg():
    fres_prime = await getUpcomingContestListgfg()
    channel = bot.get_channel(int(os.getenv("ANNOUNCEMENT_CHANNEL_ID")))
    date_format = '%b. %d, %Y'   
    for f in fres_prime:
        embed=disnake.Embed(
            title=f['Event'],
            description=f['Event'],
            url="https://clist.by/resource/geeksforgeeks.org/",
            color=disnake.Color.blurple(),
            #timestamp=datetime.strptime(f['Date'], date_format).timestamp()
             )  
     

        if channel:
            await channel.send(embed=embed)
        else:
            print("Channel not found.")


async def schedule():
    while True:
        await showContestListgfg()
        await asyncio.sleep(
            43200
        )  # pycron -> run at a specific time, this approach -> run after 12 (12 * 60 * 60 = 43200) hours each.


@bot.event
async def on_ready():
    bot.loop.create_task(schedule())
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    pass


bot.run(discord_token)