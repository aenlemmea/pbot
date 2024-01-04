import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import pycron as cron

from handlers.codeforces_handler import getUpcomingContestList

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


async def showContestList():
    fres_prime = await getUpcomingContestList()
    channel = bot.get_channel(1189825652824752189)
    if channel:
        await channel.send(fres_prime)
    else:
        print("Channel not found.")


async def schedule():
    while cron.is_now(
        "40 23 * * *"
    ):  # TODO: Adjust Timings. Currently tested on the cron string '* * * * *'
        await showContestList()


@bot.event
async def on_ready():
    bot.loop.create_task(schedule())
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    pass


bot.run(discord_token)
