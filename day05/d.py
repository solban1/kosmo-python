"""Beautiful Soup + requests + Naver Finance"""
from io import StringIO

import matplotlib.pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup, Tag
from matplotlib import font_manager, rc

url = "https://finance.naver.com/item/sise_day.naver?code=005930"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://finance.naver.com/item/sise.naver?code=005930",
}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, "lxml")

pgrr = soup.find("td", class_="pgRR")
assert isinstance(pgrr, Tag)
assert isinstance(pgrr.a, Tag)
href = pgrr.a["href"]
assert isinstance(href, str)
last_page = href.split("=")[-1]

df = pd.DataFrame()  # pandas table
base_url = "https://finance.naver.com/item/sise_day.naver?code=005930"
for page in range(1, int(last_page) + 1):
    # for page in range(1, 3):
    page_url = f"{base_url}&page={page}"
    response = requests.get(page_url, headers=headers)
    src = response.text
    # print(src)
    html = pd.read_html(StringIO(src), header=0)[0]
    df = pd.concat([df, html])

df = df.dropna()  # drop missing values
# print(df.to_string())
# print(df.iloc[0, 1])
# print(df.sort_values(by="날짜"))

plt.title("Samsung Electronics")
plt.xticks(rotation=90)
plt.grid(color="gray", linestyle="--")
plt.plot(df["날짜"], df["종가"], "ro-")
plt.show()
