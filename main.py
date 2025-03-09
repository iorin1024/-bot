import os
from dotenv import load_dotenv
load_dotenv()
import discord
from discord import app_commands
from datetime import time, timezone, timedelta
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

JST = timezone(timedelta(hours=+9), "JST")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
GUILD_ID = int(os.getenv("GUILD_ID"))

times = [
    time(hour=8, minute=30, tzinfo=JST),
    time(hour=20, minute=30, tzinfo=JST)
]

@tasks.loop(time=times)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('ﾊﾁｼﾞﾊｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧﾝﾝ!!!!!!!!!!!!')
    await channel.send(file=discord.File("8時半.mp3"))
    await asyncio.sleep(60)

@client.event
async def on_ready():
    print('on ready')
    loop.start()
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Synced slash commands")

@tree.command(name="kaibun", description="日本の政治を安定させます！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！れ")
@discord.app_commands.guilds(GUILD_ID)
async def kaibun(ctx : discord.Interaction):
    await ctx.response.send_message(f'安定しました！')

@tree.command(name="stable", description="日本の政治を安定させます！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！れ")
@discord.app_commands.guilds(GUILD_ID)
async def stable(ctx : discord.Interaction):
    await ctx.response.send_message(f'安定しました！')

TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill")
