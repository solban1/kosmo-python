"""copy one file"""
import sys

if len(sys.argv) != 3:
    print(f"usage: {__file__} source destination")
    sys.exit()

try:
    with open(sys.argv[1], "rb") as src, open(sys.argv[2], "xb") as dest:
        dest.write(src.read())
except FileExistsError as e:
    print("파일 이미 존재:", e)
except OSError as e:
    print("IO 실패:", e)
