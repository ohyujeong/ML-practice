import urllib.request
import urllib.parse

api = "https://search.naver.com/search.naver"
values = {
    "where":"nexearch",
    "sm":"top_hty",
    "fbm":"1",
    "ie":"utf8",
    "query":"초콜릿"
}
parmas = urllib.parse.urlencode(values)
url = api + "?" + parmas

data = urllib.request.urlopen(url).read()
text = data.decode("utf-8")
print(text)