import discord
from discord import app_commands,ui
from discord.ext import tasks 
import asyncio
import os
from keep_alive import keep_alive
from dotenv import load_dotenv

CHANNEL_ID = os.getenv("CHANNEL_ID")
SERVER_ID = os.getenv("SERVER_ID")

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

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
    await tree.sync(guild=discord.Object(id={SERVER_ID}))
    loop.start()

@tree.command(name="怪文書生成",description="ルイズ構文を使用した怪文書を簡単に作れます")
@discord.app_commands.guilds({SERVER_ID})
async def kaibun(interaction : discord.interaction):


TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)

