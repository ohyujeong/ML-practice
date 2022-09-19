import urllib.request
from bs4 import BeautifulSoup

import time

url = "https://news.daum.net/digital#1"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")
results = soup.select("ul.list_newsmajor li strong a.link_txt")

# for result in results:
#     print(result.string)
for result in results:
    # print(result.string)
    print(result.string)
    # print(result.attrs["href"])
    # print("")
    url_article = result.attrs["href"]
    response = urllib.request.urlopen(url_article)
    soup_article = BeautifulSoup(response, "html.parser")
    content = soup_article.find('p', attrs={'dmcf-ptype':'general'})
    
    # #string 안 되면 contents
    print(content.contents)
    # #1초 휴식
    time.sleep(1)