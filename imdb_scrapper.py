import random
import requests
from bs4 import BeautifulSoup

#url = 'https://www.imdb.com/chart/top'
#url = 'https://www.imdb.com/chart/top?sort=us,desc&mode=simple&page=1'
url = 'https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=4da9d9a5-d299-43f2-9c53-f0efa18182cd&pf_rd_r=THGQYRBDG4GYSQWMZ2GR&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2'

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,'html.parser')
movietags = soup.select('td.titleColumn')
inner_movietags = soup.select('td.titleColumn a')
rating_tags = soup.select('td.posterColumn span[name=ir]')

def get_year(movie_tag):
    moviesplit = movie_tag.text.split()
    return moviesplit[-1]

years = [get_year(tag) for tag in movietags]
actors_list = [tag['title'] for tag in inner_movietags]
titles = [tag.text for tag in inner_movietags]
ratings = [tag['data-value'] for tag in rating_tags]

n_movies = len(titles)
print(n_movies)
while(True):
    idx = random.randrange(0,n_movies)
    print(f'{titles[idx]} {years[idx]}, rating: {ratings[idx]}, starring: {actors_list[idx]} ')
    user_input = input('do you want another movien(y/[n]) ? ')

    if user_input != 'y':
        break





#print(movietag0)
