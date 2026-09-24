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
    logging.info("DB is running")
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

@bot.command(name="help")
async def help(ctx):
    embed = discord.Embed(
        title="Information",
        color=discord.Color.green()
    )
    embed.add_field(
        name = "What is this bot?",
        value = f"This is a bot that you can set `traps` for malicious bots spams. These bots created to spam every channel in a server. By settings a `trap` channel, this bot can find and kick these spammers",
        inline=False
    )
    embed.add_field(
        name = "How can you use this?",
        value = 
        f"""
        You can set trap channel by using `!setbannedchannel *channel tag*`
        If you forgot what channel was it, you can check it by `!getbannedchannel`
        """
        ,
        inline=False
    )
    await ctx.reply(embed=embed)



@bot.command(name="setbannedchannel")
@commands.has_permissions(ban_members = True, kick_members = True)
async def setbannedchannel(ctx, channel: discord.TextChannel):
    server = ctx.guild
    await db.execute("UPDATE esass SET banned_channel_id = ? WHERE server_id = ?", (channel.id, server.id))
    await db.commit

@setbannedchannel.error
async def setbannedchannelError(ctx, error):
    if isinstance(error, commands.ChannelNotFound):
        await ctx.send("Channel not found")
    elif isinstance(error,commands.MissingPermissions):
        await ctx.send("You cant set this without ban permission")

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