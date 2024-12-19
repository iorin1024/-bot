import discord
from datetime import datetime
from discord.ext import tasks 
import asyncio
import os
from keep_alive import keep_alive

TOKEN = "MTMwNTQ4MzkzMTAzMzc5NjYyOQ.Gh8MPC.ll6KRL67dVMLBP7rciVAiaVKQ7XkZQMEIWN1C8"
CHANNEL_ID = 1318500728691752980

client = discord.Client(intents=discord.Intents.all())

datalist = [
'8:30',
'20:30',
]

@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now in datalist :
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('ﾊﾁｼﾞﾊｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧﾝﾝ!!!!!!!!!!!!')

@client.event
async def on_ready():
    print('on ready')
    loop.start()


TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)

