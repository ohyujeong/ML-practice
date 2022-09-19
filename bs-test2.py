import urllib.request
from bs4 import BeautifulSoup

import time

url = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("#section_body a")

# results = soup.select("span.cluster_head_sub_topic")

for result in results:
    # print(result.string)
    print(result.attrs["title"])
    url_article = result.attrs["href"]
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.select_one("articleBodyContents")
    
    #string 안 되면 contents
    print(content.contents)
    #1초 휴식
    time.sleep(1)