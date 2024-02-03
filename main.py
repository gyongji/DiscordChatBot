import discord  # Discord 패키지 불러오기
from discord.ext import commands
# from PyKakao import DaumSearch  # PyKakao 라이브러리의 DaumSearch 클래스 import
# import json         # json 모듈 import
import requests     # 통신모듈 (request) import

# Discord Bot
file = open('TOKEN.txt', 'r')    # 만들어 둔 Discord Bot의 TOKEN을 넣은 TOKEN.txt 파일 불러와서 읽기
tk = file.read()
file.close()
# CHANNEL_ID = '<1202097779800035380>'  # 만들어 둔 Discord Server 내 Bot을 불러올 채팅 채널의 CHANNEL ID
bot = commands.Bot(command_prefix='#', intents=discord.Intents.all())  # 어떤 Bot을 만들 것인지. 명령어 실행을 '#'으로 하겠다는 코드

# Kakao Book API
file = open('KAKAO RestAPI Key.txt', 'r')   # 발급받았던 KAKAO의 RestAPI Key를 넣은 KAKAO RestAPI Key.txt 파일 불러와서 읽기
ky = file.read()
file.close()

url = "https://dapi.kakao.com/v3/search/book"   # KAKAO 책 검색 GET 메서드의 URL
apikey = ky     # KAKAO RestAPI Key 넣어둔 변수(ky) 호출해서 apikey에 넣기
subject = "파이썬"     # 검색할 단어 변수에 넣기
headers = {
    "Authorization": 'KakaoAK {}'.format(apikey)
}
data = {"query":subject}

response = requests.get(url, headers=headers, data=data)
print(response.status_code)

if response.status_code == 200:             # status code 값이 200(success)이라면
    print("======= [meta] =======")
    print(response.json()['meta'])          # meta값 출력
    print("======= [documents] =======")
    print(response.json()['documents'])     # documents값 출력

@bot.event  # 이벤트 함수 제작
async def on_ready():   # async : 비동기로 실행되는 함수 / on_ready : 봇이 시작될 때 실행되는 이벤트 함수
    print(f'Login bot: {bot.user}')

@bot.command()  # command 함수 제작
async def hello(message):   # def hello : 대화창에 '#hello'를 입력했을 경우 실행되는 함수
    await message.channel.send('Hello world!')  # '#hello' 메시지가 온 채널에 'Hello world!'를 보냄

bot.run(tk) # 만들어 둔 Discord Bot의 TOKEN 입력