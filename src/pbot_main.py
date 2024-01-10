import os
import asyncio
import disnake

from dotenv import load_dotenv
from disnake.ext import commands
from datetime import datetime

from handlers.codeforces_handler import getUpcomingContestList
from handlers.gfg_scrap import getUpcomingContestListgfg

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")


async def showContestListgfg():
    fres_prime = await getUpcomingContestListgfg()
    channel = bot.get_channel(int(os.getenv("ANNOUNCEMENT_CHANNEL_ID")))
    date_format = "%b. %d, %Y"
    for f in fres_prime:
        embed = disnake.Embed(
            title=f["Event"],
            description=f["Event"],
            url="https://clist.by/resource/geeksforgeeks.org/",
            color=disnake.Color.blurple(),
            # timestamp=datetime.strptime(f['Date'], date_format).timestamp()
        )
        if channel:
            await channel.send(embed=embed)
        else:
            print("Channel not found.")


# TODO: Figure out a common interface to handle both of the functions showContestList() and showContestListgfg() as one.


async def showContestList():
    fres_prime = await getUpcomingContestList()
    channel = bot.get_channel(int(os.getenv("ANNOUNCEMENT_CHANNEL_ID")))

    for f in fres_prime:
        embed = disnake.Embed(
            title=f.name,
            description=f.id,
            url="https://codeforces.com/contest/" + str(f.id),
            color=disnake.Color.blurple(),
            timestamp=datetime.fromtimestamp(f.startTimeSeconds),
        )

        if channel:
            await channel.send(embed=embed)
        else:
            print("Channel not found.")


async def schedule():
    while True:
        await showContestListgfg()
        await showContestList()
        await asyncio.sleep(
            43200
        )  # pycron -> run at a specific time, this approach -> run after 12 (12 * 60 * 60 = 43200) hours each from starting time.


@bot.event
async def on_ready():
    bot.loop.create_task(schedule())
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    pass


bot.run(discord_token)
