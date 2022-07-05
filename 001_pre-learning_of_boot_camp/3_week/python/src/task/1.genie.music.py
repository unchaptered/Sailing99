# rank / title / artist
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# rank '#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number'
# title '#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis'
# artist '#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis'

data = requests.get(
    'https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',
    headers = headers
)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    target = music.select_one('td.info > a.title.ellipsis')
    if target is not None:
        title = target.text.strip()
        rank = music.select_one('td.number').text[0:2].strip()
        artist = music.select_one('td.info > a.artist.ellipsis').text.strip()
        print(rank, title, artist)
