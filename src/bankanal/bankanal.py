import discord
import asyncio
import logging 
import sqlite3
import os
from discord.ext import commands
from dotenv import load_dotenv

# -------------------------------------------------------------------------

load_dotenv()

logging.basicConfig(  #maybe?
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="w"
)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents = intents, help_command=None)


db = sqlite3.connect("amazing.db")
cursor = db.cursor()
bot.db = db 

#--------------------------------------------------------


async def main() -> None:
    await bot.start(os.getenv("BOTSS"))

def run():
    asyncio.run(main())

if __name__ == "__main__":
    logging.info("--------------Basladi--------------")
    run()