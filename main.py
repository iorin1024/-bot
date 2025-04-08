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

CHANNEL_ID = 1359072420736274592
GUILD_ID = 1241632837526884432

times = [
    time(hour=8, minute=0, tzinfo=JST)
]

subjects = []
dates = []
contents = []

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

@tree.command(name="ping", description="課題の教科、内容、日付などを入力して管理します")
@app_commands.describe(name="キャラクター名をここに入力")
@discord.app_commands.choices(
    subject=[
        discord.app_commands.Choice(name="英語B",value="英語B")
    ]
)
@discord.app_commands.guilds(GUILD_ID)
async def add(ctx : discord.Interaction,subject:str,date:str,content:str):
    print(subject)
    print(date)
    print(content)

TOKEN = "MTM1OTA3MjcxMjE1NjI1MDEyMw.GfUvoz.cwKjYNiq-xwCLL9Xa-q0Wxw1EOny3MHYWsdQ3I"

keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill")
