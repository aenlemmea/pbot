import disnake
from disnake.ext import commands
import os
import asyncio
from disnake.ext import commands
from datetime import datetime
from dotenv import load_dotenv
from handlers.gfg_scrap import getUpcomingContestListgfg
from handlers.codechef_scraper import getUpcomingContestListchef

load_dotenv()
discord_token = os.getenv('discord_token')

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents) 

async def showContestListgfg():
    fres_prime = await getUpcomingContestListgfg()
    channel = bot.get_channel(int(os.getenv("ANNOUNCEMENT_CHANNEL_ID")))
    #date_format = ' %b. %d, %Y '   
    for f in fres_prime:
        embed=disnake.Embed(
            title=f['Event Title'],
            description="Start/End time:"+f['Start Time']+" "+"Duration:"+f['Duration']+" "+"Time left:"+f['Time Left'],
            url="https://clist.by/?resource=126&view=list&group=no&status=coming",
            color=disnake.Color.blurple(),
            #timestamp=datetime.strptime(f['Date'], date_format).timestamp()
             )  
     

        if channel:
            await channel.send(embed=embed)
        else:
            print("Channel not found.")




async def showContestListchef():
    fres_prime = await getUpcomingContestListchef()
    channel = bot.get_channel(int(os.getenv("ANNOUNCEMENT_CHANNEL_ID")))
     
    for f in fres_prime:
        embed=disnake.Embed(
            title=f['Contest Name'],
            description="Start time:"+f['Start Time']+" "+"Duration:"+f['Duration']+" "+"Remaining Time:"+f['Remaining Time']+" "+"Contest Code:"+f['Contest Code']+" "+"Additional Info:"+f['Additional Info'],
            url="https://clist.by/?resource=126&view=list&group=no&status=coming",
            color=disnake.Color.blurple(),
            
             )  
     

        if channel:
            await channel.send(embed=embed)
        else:
            print("Channel not found.")


async def schedule():
    while True:
        await showContestListgfg()
        await showContestListchef()
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