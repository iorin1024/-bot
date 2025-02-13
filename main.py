import os
from dotenv import load_dotenv
load_dotenv()
import discord
from datetime import time, timezone, timedelta
from discord.ext import tasks, commands
import asyncio
from keep_alive import keep_alive

intents = discord.Intents.all()
client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(intents=intents, command_prefix="!")
tree = bot.tree


JST = timezone(timedelta(hours=+9), "JST")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

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
    await tree.sync()
    print("Synced slash commands")

@tree.command(name="日本の政治を安定させる機能", description="日本の政治を安定させます！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！れ")
async def kaibun(ctx : discord.Interaction):
    await ctx.response.send_message(f'安定しました！')

TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill")
