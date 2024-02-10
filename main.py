import discord  # Discord 패키지 불러오기
from discord.ext import commands
import dotenv
import os
import requests     # 통신모듈 (request) import
import traceback    # 에러 메시지를 활용하기 위한 모듈 import
import time         # sleep 사용하기 위한 모듈 import


# 환경 변수 #
dotenv_Discord_TOKEN = dotenv.load_dotenv('Discord TOKEN.env')
dotenv_KAKAO_RestAPI_KEY = dotenv.load_dotenv('KAKAO RestAPI KEY.env')
# Discord Bot
Discord_TOKEN = os.environ.get('TOKEN')
BOT = commands.Bot(command_prefix='&', intents=discord.Intents.all())
# Kakao Book API
KAKAO_RestAPI_KEY = os.environ.get('API_KEY')


# 상수 및 함수 선언 #
KAKAO_API_BOOK_URL = "https://dapi.kakao.com/v3/search/book"
REQUEST_HEADERS = {
    "Authorization": 'KakaoAK {}'.format(KAKAO_RestAPI_KEY)
}
LIST_SIZE = 5
BOT_NAME = "BookManager"
ERROR_MASSAGE = "검색 결과가 없습니다.\n혹시 오타가 났나요? 다시 검색해 보세요!"
MAG_MASSAGE = "원하던 결과가 나오지 않았나요?\n 조금 더 자세히 검색해 보세요!"

# KAKAO API Request
def request(query, target):
    request_query_parameter = {"query": query, "size": LIST_SIZE, "target": target}
    response = requests.get(KAKAO_API_BOOK_URL, headers=REQUEST_HEADERS, data=request_query_parameter)
    return response.json()['documents'], response.json()['meta']['total_count']

# embed_footer
async def embed_with_footer(embed, message):
    embed.set_footer(text=BOT_NAME)
    await message.send(embed=embed)

# except
async def except_print(ctx, e):
    await ctx.send(ERROR_MASSAGE)
    print(e)


# 기능 #
# Discord Bot 명령어 Error 시 출력
@BOT.event
async def on_command_error(ctx, error):
    trace_back = traceback.format_exception(type(error), error, error.__traceback__)
    error_line = [line.rstrip() for line in trace_back]
    error_string = '\n'.join(error_line)
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("명령어를 잘못 입력하셨나요? 다시 확인해보세요.")
    else:
        print(error_string)

# Discord Bot 기본 상태
@BOT.event
async def on_ready():   # async : 비동기로 실행되는 함수 / on_ready : 봇이 시작될 때 실행되는 이벤트 함수
    print(f'Login bot: {BOT.user}')     # 봇이 실행될 때 터미널에 'Login bot: BookManager#1059' 출력
    await BOT.change_presence(activity=discord.Game(name="책 정리"))   # 봇이 실행되어 온라인이 되면 '책 정리 하는 중'이 상태메세지에 표시

# 인사 출력 (hello)
@BOT.command()
async def hello(message):   # def hello : 대화창에 '&hello'를 입력했을 경우 실행되는 함수
    embed = discord.Embed(title=f":woman_raising_hand:  Hello world!", description=f"반가워요. {BOT_NAME}입니다.",
                          color=discord.Color.green())
    embed.add_field(name=f'제 사용법이 궁금하신가요?', value=f"&aid 를 입력해 보세요!", inline=False)
    await embed_with_footer(embed, message)

# 사용법 출력 (aid)
@BOT.command()
async def aid(message):
    embed = discord.Embed(title=f":clipboard:  Hello world!", description=f"절 사용하는 방법을 알려드릴게요.",
                          color=discord.Color.green())
    embed.add_field(name=f'▶  명령어 입력 방법 : &', value=f"모든 명령어는 &(앰퍼샌드) 기호를 사용하여 입력해요.", inline=False)
    embed.add_field(name=f'▶  t 책 제목', value=f"해당 제목의 도서를 최대 5개까지 검색해 줘요.", inline=False)
    embed.add_field(name=f'▶  a 저자', value=f"해당 저자의 도서를 최대 5개까지 검색해 줘요.\n저자와 역자를 하나로 취급하니 참고해 주세요!", inline=False)
    embed.add_field(name=f'▶  b 책 제목_저자', value=f"해당하는 도서의 상세 정보를 알려줘요.", inline=False)
    await embed_with_footer(embed, message)

# 이스터에그
@BOT.event
async def on_message(message):
    message_content = message.content
    if message_content == "야":
        await message.channel.send("왜")
    elif message_content == "랩":
        await message.channel.send("북치기 박치기")
    elif message_content == "아재개그":
        await message.channel.send("책이 죽어서 가는 곳은?")
        time.sleep(3)
        await message.channel.send("도서관")
        await message.channel.send("파항항 ꉂꉂ(ᵔᗜᵔ*) 파항항 ꉂꉂ(ᵔᗜᵔ*) 파항항 ꉂꉂ(ᵔᗜᵔ*) 파항항 ꉂꉂ(ᵔᗜᵔ*)")
    await BOT.process_commands(message)

# 제목 검색
@BOT.command()
async def t(ctx, *args):  # 제목(title)를 검색하면 실행되는 함수
    try:
        title_spacing = " ".join(args)  # 띄어쓰기가 포함된 처리
        documents, total_count_meta = request(title_spacing, "title")

        embed = discord.Embed(title=f":closed_book:  제목({title_spacing})으로 검색하셨군요?",
                              description=f"{title_spacing} 도서 리스트\n검색된 도서 {total_count_meta}개",
                              color=discord.Color.red())

        for i in range(5):
            title_documents = documents[i]['title']
            authors_documents = documents[i]['authors']

            # 작가 리스트 대괄호 및 따옴표 없이 출력하기
            authors_no_special_characters = str(authors_documents)[1:-1]
            authors_no_special_characters = authors_no_special_characters.replace("'", "")

            embed.add_field(name=f'{i+1}. {title_documents} - {authors_no_special_characters}', value='', inline=False)

        embed.add_field(name=f':mag:', value=MAG_MASSAGE, inline=False)
        await embed_with_footer(embed, ctx)

    except Exception as e:  # 예외가 발생했을 시 실행됨
        await except_print(ctx, e)

# 저자 검색
@BOT.command()
async def a(ctx, *args):  # 저자(author)를 검색하면 실행되는 함수
    try:
        authors_spacing = " ".join(args)  # 띄어쓰기가 포함된 처리
        documents, total_count_meta = request(authors_spacing, "person")

        embed = discord.Embed(title=f":blue_book:  저자({authors_spacing})로 검색하셨군요?",
                              description=f"{authors_spacing} 작가의 도서 리스트\n검색된 도서 {total_count_meta}개",
                              color=discord.Color.blue())

        for i in range(5):
            title_documents = documents[i]['title']
            authors_documents = documents[i]['authors']

            # 작가 리스트 대괄호 및 따옴표 없이 출력하기
            authors_no_special_characters = str(authors_documents)[1:-1]
            authors_no_special_characters = authors_no_special_characters.replace("'", "")

            embed.add_field(name=f'{i+1}. {authors_no_special_characters} - {title_documents}', value='', inline=False)

        embed.add_field(name=f':mag:', value=MAG_MASSAGE, inline=False)
        await embed_with_footer(embed, ctx)

    except Exception as e:  # 예외가 발생했을 시 실행됨
        await except_print(ctx, e)

# 제목_저자 검색
@BOT.command()
async def b(ctx, *args):  # 책 제목을 검색하면 실행되는 함수
    try:
        book_spacing = " ".join(args)  # 띄어쓰기가 포함된 처리

        # book 값에서 언더바(_)를 기준으로 제목/저자 구분하기
        search_book = book_spacing.split('_')
        book_title = search_book[0]   # 제목
        book_authors = search_book[1]  # 저자

        documents, total_count_meta = request({book_title, book_authors}, {"title", "person"})
        url_documents = documents[0]['url']

        embed = discord.Embed(title=f":green_book:  저자 \'{book_authors}\'의 도서 \'{book_title}\'(을)를 검색하셨군요?",
                              url=url_documents,
                              description=f"도서 검색 봇 BM이 도서 정보를 알려드립니다!\n검색된 도서 {total_count_meta}개",
                              color=discord.Color.green())
        title_documents = documents[0]['title']
        thumbnail_documents = documents[0]['thumbnail']
        authors_documents = documents[0]['authors']
        publisher_documents = documents[0]['publisher']
        contents_documents = documents[0]['contents']

        # 작가 리스트 대괄호 및 따옴표 없이 출력하기
        authors_no_special_characters = str(authors_documents)[1:-1]
        authors_no_special_characters = authors_no_special_characters.replace("'", "")

        embed.add_field(name=f'제목', value=title_documents, inline=False)
        embed.add_field(name=f"저자", value=authors_no_special_characters, inline=True)
        embed.add_field(name=f"출판사", value=publisher_documents, inline=True)
        embed.add_field(name=f'도서 소개', value=contents_documents + "...", inline=False)
        embed.set_image(url=thumbnail_documents)

        embed.add_field(name=f':mag:', value=MAG_MASSAGE, inline=False)
        await embed_with_footer(embed, ctx)

    except Exception as e:  # 예외가 발생했을 시 실행됨
        await except_print(ctx, e)


# BOT 실행 #
BOT.run(Discord_TOKEN)     # 만들어 둔 Discord Bot의 TOKEN 입력