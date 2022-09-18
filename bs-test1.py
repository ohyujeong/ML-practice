import urllib.request
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, "html.parser")

results = soup.select("span.value")
print("달러: ", results[0].string) #원달러 환율
print("엔: ", results[1].string) #원엔 환율
print("유로: ",results[2].string) #원유로 환율

# for result in results:
#     print(result.string)