import os

for f in os.scandir():
    print(f)
    print(type(f))
