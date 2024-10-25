from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

user = "Mozilla/5.0 (IPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15(KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1"

options_ = Options()
options_.add_argument(f"user-agent={user}")
options_.add_experimental_option("detach", True)
options_.add_experimental_option("excludeSwitches", ["enable-logging"])


# # 크롬 드라이버 매니저를 자동으로 설치되도록 실행시키는 코드
# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=options_)

url = "https://m2.melon.com/index.htm"
driver.get(url)
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR, ".link-logo").click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='naviMenu']/nav/ul/li[3]/a").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".main_chart").find_element(
    By.CSS_SELECTOR, "#moreBtn"
).click()
time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
chartList = soup.select_one("#_chartList")
list_items = chartList.select(".list_item")

for item in list_items:
    rank = item.select_one(".ranking_num").text
    title = item.select_one(".title.ellipsis").text
    singer = item.select_one(".name.ellipsis").text
    print(f"순위 : {rank}")
    print(f"제목 : {title.strip()}")
    print(f"가수 : {singer}")
    print()

# 아래 순서대로 스크래핑한 자료를 출력해주세요
# 순위 :
# 노래 제목 :
# 가수 이름 :

driver.quit()
