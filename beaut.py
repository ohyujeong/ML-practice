# 라이브러리 읽어 들이기 --- (※1)
from bs4 import BeautifulSoup
# 분석하고 싶은 HTML --- (※2)

#태그 선택자
"h1"
"html"

#아이디 선택자
"#<아이디 이름>"

#클래스 선택자 (여러개 사용 가능)
".<클래스 이름>.<클래스 이름>.<클래스 이름>"
#공백 없이 조합

#구조 선택자(후손, 자식)
"html li" #후손
"ul.items > li" #자식

html = """
<html>
    <body>
    <div id="meigen">
        <h1> 위키북스 도서 </h1>
        <ul class = "items art it book">
            <li> 유니티 게임 이펙트 입문</li>
            <li> 스위프트로 시작하는 아이폰 앱 개발 교과서</li>
            <li> 모던 웹사이트 디자인의 정석</li>
        </ul>
    </div>
    </body>
</html>
"""
# HTML 분석하기 --- (※3)
soup = BeautifulSoup(html, 'html.parser')


# 원하는 부분 추출하기 --- (※4)
header = soup.select_one("h1") #요소
list_items = soup.select("ul.items > li") #요소의 배열

print(header.string)
print(soup.select_one("ul").attrs) #ul 태그의 속성 출력
for li in list_items:
    print(li.string)