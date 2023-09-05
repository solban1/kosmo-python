import requests
from bs4 import BeautifulSoup

url = "https://www.nate.com"
r = requests.get(url)
src = r.text

soup = BeautifulSoup(src, "html.parser")
result = soup.select("#olLiveIssueKeyword span.txt_rank")

for tag in result:
    print(tag.text)
