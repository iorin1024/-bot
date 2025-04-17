import os
from dotenv import load_dotenv
load_dotenv()
import discord
from discord import app_commands
import datetime 
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
GUILD_ID = int(os.getenv("GUILD_ID"))

times = [
    datetime.time(hour=6, minute=00, tzinfo=JST)
]

subjects = []
dates = []
contents = []

@tasks.loop(time=times)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    dtnow = datetime.datetime.now()
    for i, (subjectss, datess, contentss) in enumerate(zip(subjects,dates,contents)):
        datesss = datess.split('/')
        print(datesss)
        b = []
        for i in datesss:
            b.append(int(i))
        finishdate = datetime.datetime(b[0],b[1],b[2])
        result = finishdate - dtnow
        if  int(result.days) <= 3 and int(result.days) >= 0:
            embed = discord.Embed(title="教科名",description=subjectss,color=0xff0000)
            embed.add_field(name="締切日",value=datess)
            embed.add_field(name="課題内容",value=contentss)
            await channel.send(embed=embed)
    await asyncio.sleep(60)

@client.event
async def on_ready():
    print('on ready')
    loop.start()
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Synced slash commands")


@tree.command(
    name="addhomework",#コマンド名
    description="課題、日付、内容を登録してリマインドします"#コマンドの説明
)
@app_commands.describe(subject="該当する教科を登録")
@app_commands.describe(date="締切日を登録。例:2025/10/24")
@app_commands.describe(content="課題内容を登録")
@discord.app_commands.choices(
    subject=[
        discord.app_commands.Choice(name="英語B",value="英語B")
    ]
)
@discord.app_commands.guilds(GUILD_ID)
async def add(ctx : discord.Interaction,subject:str,date:str,content:str):
    subjects.append(subject)
    dates.append(date)
    contents.append(content)
    await ctx.response.send_message("登録しました！")

TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill")
