import os
import sys

while True:
    path = input("> ").strip()
    if len(path) == 0:
        continue
    if path == "exit":
        sys.exit()
    elif not os.path.exists(path):
        print(path + ": 존재하지 않는 경로")
    elif os.path.isfile(path):
        print(path + ": 파일임")
    elif os.path.isdir(path):
        for d in os.listdir(path):
            print(d)
    else:
        print("알 수 없는 오류")
