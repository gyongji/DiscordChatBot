<div align="center">
<H1>👾 Discord Bot BM: BookManager 👾</H1>
<img src="https://github.com/gyongji/DiscordChatBot/assets/152964778/1dd4c139-298a-4528-87e6-a5edcdffc7df" width="300" height="300"/>
</div>
<br>

# 📌 Description
> 찾고 싶은 도서를 검색할 수 있는 디스코드 봇입니다.
> 도서의 제목을 검색하면 검색한 제목의 도서 리스트를, 저자를 검색하면 해당 저자가 작성한 도서를 리스트로 출력합니다.
> 도서의 제목과 저자를 함께 검색하면 해당 도서에 대한 정보를 제공합니다.
> 
> This Discord bot where you can search for the books you want to find.
> When you search for the title of a book, you print out a list of books with the title you searched for,
> and when you search for an author, you print out the book written by that author as a list.
> If you search for the title and author of the book together, will provide information about that book.
<br>

# 💾 Environment
```
Writed OS : Windows
Using Language : Python
```

# 🎮 Prerequisite
### - Using Modules
```Python
import discord
from discord.ext import commands
import dotenv
import os
import requests
import traceback
import time
```
### - Using API
```
Discord Developer
Kakao Developers
```

# 💻 Usage
> 이 봇을 복제하고 실행하려면 [Git](https://git-scm.com/downloads)과 [Python](https://www.python.org/downloads/)을 설치해야 합니다. <br>
> To clone and run this Bot, you'll need [Git](https://git-scm.com/downloads) and [Python](https://www.python.org/downloads/) installed on your computer.
## 1. Create Discord Bot
**Discord Bot을 만들어야 합니다.** Discord 로그인 후 [여기](https://discord.com/developers/applications)에서 만들 수 있습니다. <br>
[이 링크](https://discord.com/developers/applications)에서 파란색 버튼 '시작'을 누르면 봇을 만드는 방법을 알 수 있습니다! <br>

**You need to create a Discord bot.** After logging in to Discord, You can create one from [here](https://discord.com/developers/applications). <br>
Press the blue button 'Start' on [this link](https://discord.com/developers/docs/intro) and you'll know how to create a bot!

## 2. Obtain Kakao API keys
**Kakao API Key를 발급받아야 합니다.** [이 링크](https://developers.kakao.com/)에서 로그인 후 '내 애플리케이션'을 눌러 진행할 수 있습니다.<br>
API사용 방법은 [여기](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-book)에서 볼 수 있습니다.

**You need to get the Kakao API Key.** You can log in at [this link](https://developers.kakao.com/) and click 'My application' to proceed.<br>
You can find instructions on how to use the API at [here](https://developers.kakao.com/docs/latest/ko/daum-search/dev-guide#search-book).

## 3. Clone this repository
```
$ git clone https://github.com/gyongji/DiscordChatBot.git
```
## 4. Module Download
Install with pip:
```
$ pip install -r requirements.txt
```

# 📋 BM Command
> {  }(중괄호)는 입력하지 마세요.<br>Do not enter {  }(middle brackets).
> 
Command|Explain
---|---
&hello|인사<br>Greetings
&aid|도움말<br>help
&t {book title}|해당 제목을 가진 도서들을 리스트로 추출 (5개)<br>Extract books with corresponding titles into a list (Five)
&a {book author}|해당 저자가 작성한 도서들을 리스트로 추출 (5개)<br>Extracted books written by the author of the relevant into a list (Five)
&b {book title_book author}|해당 도서의 정보 출력<br>Print out the information of the relevant book
Easter egg|특정 단어를 입력하면 BM이 대답해요!<br>If you type in a specific word, BM will answer it!
