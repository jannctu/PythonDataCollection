from selenium.webdriver import Chrome
from selenium import webdriver
from instascrape import Profile, scrape_posts, Post

username='jankristanto_'
#browser = webdriver.Chrome('C:/Users/Tro/Downloads/chromedriver_win32/chromedriver.exe')
webdriver = Chrome("C:/Users/Tro/Downloads/chromedriver_win32/chromedriver.exe")

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=YOUR_SESSION_ID"
}
pr = Profile(username)
pr.scrape(headers=headers)
#posts = pr.get_recent_posts()
posts = pr.get_posts(webdriver=webdriver, login_first=True)
scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=0.5, silent=False)

for post in scraped_posts:
    fname = post.upload_date.strftime("%Y-%m-%d %Hh%Mm")
    post.download(f"{fname}.png")


