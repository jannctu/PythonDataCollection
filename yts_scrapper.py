import random
import requests
from bs4 import BeautifulSoup

url = 'https://yts.mx/'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
#movietags = soup.select('div[id=popular-downloads]')
inner_movietags = soup.select('div.browse-movie-wrap')

popular_downloads = soup.find('div', attrs={'id': 'popular-downloads'})
popular_movies_tags = popular_downloads.find_all('div', attrs={'class': 'browse-movie-wrap'})

for movies in popular_movies_tags:
    title_tag = movies.find('a', attrs={'class': 'browse-movie-title'})
    h4_tags = movies.find_all('h4')
    img_tag = movies.find('img')
    print(title_tag.text + ' | ' + h4_tags[1].text + ', ' + h4_tags[2].text + ' | ('+ h4_tags[0].text + ') ')
    #print('https://img.yts.mx/' + img_tag['src'])