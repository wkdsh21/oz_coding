import requests
from bs4 import BeautifulSoup

header_user = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어를 하나만 입력해주세요 : ")

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

# 여기서 부터 코드를 작성해주세요
# 광고 배너의 id 또는 class 명을 찾아보세요
# 광고 배너의 결과값을 변수 담아서 if문으로 검증을 합니다.
# 아무것도 없는 경우는 어떤 값이 들어가는지 확인해주세요
# if문의 참과 거짓일 경우 어떻게 작동하는지에 대한 원리를 상기시켜보세요
for i in soup.select(".view_wrap"):
    if i.select_one(".link_ad"):
        continue
    title = i.select_one(".title_link").text
    username = i.select_one(".name").text
    print(f"검색 키워드 : {keyword}")
    print(f"블로그 제목 : {title}")
    print(f"블로그 작성자 : {username} \n")
