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
intents.message_content = True
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
    await bot.db.commit() #... i really need to execute it before commiting
#--------------------------------------------------------

@bot.command(name="salam")
async def salam(ctx):
    await ctx.send("Test")

@bot.command(name="currid")
async def currid(ctx):
    if not ctx.guild:
        await ctx.send("...Niye")
        return
    await ctx.send(f" `{ctx.guild.id }`")




#--------------------------------------------------------

async def main() -> None:
    try:
        await setup_DB()
    except Exception as e:
        logging.error(f" DB `{e}")
        return

    try:
        await bot.start(os.getenv("BOTSS"))
    finally:
        if hasattr(bot, "db"):
            await bot.db.close()


def run():
    try:
        asyncio.run(main())
    except:
        logging.info("Bot dayandi")

if __name__ == "__main__":
    logging.info("--------------Basladi--------------")
    run()