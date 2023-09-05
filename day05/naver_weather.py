import requests
from bs4 import BeautifulSoup, Tag

url = "https://weather.naver.com/"
html = requests.get(url).text
soup = BeautifulSoup(html, "lxml")

current_temp_el = soup.select_one("#now .current")
assert isinstance(current_temp_el, Tag)
current_temp = current_temp_el.contents[2]

summary_el = soup.select_one("#now .summary .weather")
assert isinstance(summary_el, Tag)
summary = summary_el.string

print(f"현재 온도는 {current_temp}도 입니다.")
print(f"오늘의 날씨는 '{summary}' 입니다.")
