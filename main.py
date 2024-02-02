import discord  # Discord 패키지 불러오기
from discord.ext import commands

file = open('TOKEN.txt', 'r')    # 만들어 둔 Discord Bot의 TOKEN을 넣은 TOKEN.txt 파일 불러와서 읽기
tk = file.read()
file.close()
# CHANNEL_ID = '<1202097779800035380>'  # 만들어 둔 Discord Server 내 Bot을 불러올 채팅 채널의 CHANNEL ID

bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())  # 어떤 Bot을 만들 것인지. 명령어 실행을 '#'으로 하겠다는 코드

@bot.event  # 이벤트 함수 제작
async def on_ready():   # async : 비동기로 실행되는 함수 / on_ready : 봇이 시작될 때 실행되는 이벤트 함수
    print(f'Login bot: {bot.user}')

@bot.command()  # command 함수 제작
async def hello(message):   # def hello : 대화창에 '#hello'를 입력했을 경우 실행되는 함수
    await message.channel.send('Hello world!')  # '#hello' 메시지가 온 채널에 'Hello world!'를 보냄

bot.run(tk) # 만들어 둔 Discord Bot의 TOKEN 입력