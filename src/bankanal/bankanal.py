import discord
import asyncio
import logging 
import aiosqlite
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


#I FORGOT ASYNC EXIST 

async def setup_DB():
    bot.db = await aiosqlite.connect("amazing.db")
    bot.db.row_factory = aiosqlite.Row 

    await bot.db.execute(
        """
        CREATE TABLE IF NOT EXISTS esass (
        server_id INTEGER PRIMARY KEY,
        banned_channel_id INTEGER DEFAULT NULL
        )
"""
    )
#--------------------------------------------------------






#--------------------------------------------------------

async def main() -> None:
    await bot.start(os.getenv("BOTSS"))

def run():
    try:
        setup_DB()
    except:
        logging.error("DB")
        return
    try:
        asyncio.run(main())
    except:
        logging.info("Bot dayandi")

if __name__ == "__main__":
    logging.info("--------------Basladi--------------")
    run()