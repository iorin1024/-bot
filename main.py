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

@tree.command(name="kaibun", description="怪文書(ルイズ構文)をお手軽に作れます。")
@app_commands.describe(name="キャラクター名をここに入力")
@app_commands.describe(fullname="フルキャラクター名をここに入力")
@app_commands.describe(haircolor="髪色をここに入力")
@app_commands.describe(location="地名をここに入力")
@app_commands.describe(genre="小説などのジャンル名をここに入力")
@app_commands.describe(volumes="何巻かなどをここに入力")
@app_commands.describe(genre2="アニメなどのジャンル名をここに入力")
@app_commands.describe(seasons="アニメ何期かなどをここに入力")
@app_commands.describe(genre3="コミックなどのジャンル名をここに入力")
@app_commands.describe(volumes2="何巻かなどをここに入力")
@app_commands.describe(kunorchan="お好きな方をどうぞ")
@app_commands.describe(where="表紙絵などどこからかここに入力")
@app_commands.describe(where2="挿絵などどこからかここに入力")
@app_commands.describe(othername1="他のキャラクター1人目の名前をここに入力")
@app_commands.describe(othername2="他のキャラクター2人目の名前をここに入力")
@app_commands.describe(othername3="他のキャラクター3人目の名前をここに入力")
@app_commands.describe(othername4="他のキャラクター4人目の名前をここに入力")
@app_commands.describe(othername5="他のキャラクター5人目の名前をここに入力")
@discord.app_commands.choices(
    kunorchan=[
        discord.app_commands.Choice(name="くん付けにする",value="くん"),
        discord.app_commands.Choice(name="ちゃん付けにする",value="ちゃん")
    ]
)
@discord.app_commands.guilds(GUILD_ID)
async def kaibun(ctx : discord.Interaction,name:str,fullname:str,haircolor:str,location:str,
                 genre:str,volumes:str,genre2:str,seasons:str,genre3:str,volumes2:str,
                 kunorchan:str,where:str,where2:str,othername1:str,othername2:str,othername3:str,othername4:str,othername5:str):
    namespace = ' '.join(list(name))
    othername3start = othername3[0]
    await ctx.response.send_message(f"""
                                    {name}！{name}！{name}！{name}ぅぅうううわぁああああああああああああああああああああああん！！！
あぁああああ…ああ…あっあっー！あぁああああああ！！！{name}{name}{name}ぅううぁわぁああああ！！！
あぁクンカクンカ！クンカクンカ！スーハースーハー！スーハースーハー！いい匂いだなぁ…くんくん
んはぁっ！{fullname}たんの{haircolor}の髪をクンカクンカしたいお！クンカクンカ！あぁあ！！
間違えた！モフモフしたいお！モフモフ！モフモフ！髪髪モフモフ！カリカリモフモフ…きゅんきゅんきゅい！！
{genre}{volumes}の{name}たんかわいかったよぅ！！あぁぁああ…あああ…あっあぁああああ！！ふぁぁあああんんっ！！
{genre2}{seasons}決まって良かったね{name}たん！あぁあああああ！かわいい！{name}たん！かわいい！あっああぁああ！
{genre3}{volumes2}も発売されて嬉し…いやぁああああああ！！！にゃああああああああん！！ぎゃあああああああああああああああ！！！
{genre3}なんて現実じゃない！！！！あ…{genre}も{genre2}もよく考えたら…
{namespace} ち ゃ ん は 現実 じ ゃ な い？にゃあああああああああああああん！！うぁああああああああああ！！
そんなぁああああああ！！いやぁぁぁあああああああああ！！はぁああああああん！！{location}ぁああああ！！
この！ちきしょー！やめてやる！！現実なんかやめ…て…え！？見…てる？{where}の{name}ちゃんが僕を見てる？
{where}の{name}ちゃんが僕を見てるぞ！{name}ちゃんが僕を見てるぞ！{where2}の{name}ちゃんが僕を見てるぞ！！
{genre2}の{name}ちゃんが僕に話しかけてるぞ！！！よかった…世の中まだまだ捨てたモンじゃないんだねっ！
いやっほぉおおおおおおお！！！僕には{name}ちゃんがいる！！やったよ{othername1}！！ひとりでできるもん！！！
あ、{genre3}の{name}ちゃああああああああああああああん！！いやぁあああああああああああああああ！！！！
あっあんああっああんあ{othername2}ぁあ！！{othername3start}、{othername3}！！{othername4}ぁああああああ！！！{othername5}ぁあああ！！
ううっうぅうう！！俺の想いよ{name}へ届け！！{location}の{name}へ届け！""")

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
