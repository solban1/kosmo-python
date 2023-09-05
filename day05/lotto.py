from collections import Counter

import requests

current_no = 1083
url = "https://www.dhlottery.co.kr/common.do"
params = {
    "method": "getLottoNumber",
}
headers = {
    "Accept": "application/json",
}

nums = []
for i in range(50):
    params["drwNo"] = str(current_no - i)
    json = requests.get(url, params=params, headers=headers).json()
    for j in range(1, 7):
        nums.append(json["drwtNo" + str(j)])

for num, count in Counter(nums).most_common():
    print(f"번호: {num}, 횟수: {count}")
