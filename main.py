import discord
from datetime import time, timezone, timedelta
from discord.ext import tasks 
import asyncio
import os
from keep_alive import keep_alive
from dotenv import load_dotenv

CHANNEL_ID = 1318500728691752980

client = discord.Client(intents=discord.Intents.all())

JST = timezone(timedelta(hours=+9), "JST")

times = [
    time(hour=16, minute=44, tzinfo=JST),
    time(hour=20, minute=30, tzinfo=JST)
]

@tasks.loop(time=times)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('ﾊﾁｼﾞﾊｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧﾝﾝ!!!!!!!!!!!!')
    await channel.send(file=discord.File(hatiji.mov))
    await asyncio.sleep(60)

@client.event
async def on_ready():
    print('on ready')
    loop.start()


TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill")
