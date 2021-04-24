import requests
from bs4 import BeautifulSoup
import pandas

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
response = requests.get("https://www.104.com.tw/jobs/search/?ro=0&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001001000&order=12&asc=0&page=1&mode=s&jobsource=2018indexpoc",headers=headers)

content = response.content
soup = BeautifulSoup(content,"html.parser")

job_rest = soup.find_all("div",attrs={"id": "js-job-content"})
list_tr = job_rest[0].find_all("article",attrs={"class": "js-job-item"})

list_rest =[]
for tr in list_tr:
    dataframe ={}
    h2_ = tr.find("h2",attrs={"class": "b-tit"})
    dataframe["title"] = (h2_.find("a",attrs={"class":"js-job-link"})).text.replace('\n', '')

    list_ul = tr.find_all("ul")
    list_li0 = list_ul[0].find_all("li")
    dataframe["company"] = (list_li0[1].find("a")).text.replace('\n', '').strip()

    list_li1 = list_ul[1].find_all("li")
    dataframe["location"] = list_li1[0].text.replace('\n', '').strip()
    list_rest.append(dataframe)

df = pandas.DataFrame(list_rest)
df.to_csv("job_in_tpe.csv",index=False)