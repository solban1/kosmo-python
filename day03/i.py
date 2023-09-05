# 디렉토리 리스팅
import os

"""
dir = 'C:\\SOO\\Python\\day03_base3'
kids = os.listdir(dir)
print(type(kids))  # list
for kid in kids:
    if os.path.isfile(dir+'\\'+kid):
        print('[F]', kid)
    else:
        print('[D]', kid)
"""

# 미션( 입력경로 존재여부 -> 파일경로와 디렉토리경로 구분 -> 디렉토리경로라면.. 리스팅! )
target = input("리스팅할 디렉토리:").strip()
# print(target)


def listMyDir(dir):
    kids = os.listdir(dir)
    print(kids)
    print(type(kids))  # list
    for kid in kids:
        if os.path.isfile(dir + "\\" + kid):
            print("[F]", kid)
        else:
            print("[D]", kid)


if os.path.exists(target):
    print("존재O")
    if os.path.isfile(target):
        print("디렉토리가 아님")
    else:
        listMyDir(target)
else:
    print("존재X")
