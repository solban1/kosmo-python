import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver"
params = {"code": "005930"}

r = requests.get(url, params=params)
src = r.text
soup = BeautifulSoup(src, "lxml")
rate = soup.select_one("div.rate_info > div.today > p.no_today > em.no_up > span.blind")
print(rate.text)
