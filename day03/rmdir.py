import os

target = input("삭제 할 디렉토리:").strip()


def removeMyDirRecursive(d):
    if os.path.isfile(d):
        os.remove(d)
    else:
        for child in os.listdir(d):
            removeMyDirRecursive(d + "/" + child)
        os.rmdir(d)


def removeMyDir(d):
    if len(os.listdir(d)) != 0 and input("디렉토리가 비어있지 않음. 그래도 삭제[y/N]? ").lower() != "y":
        return
    removeMyDirRecursive(os.path.abspath(d))


if os.path.exists(target):
    print("존재O")
    if os.path.isdir(target):
        removeMyDir(target)
    else:
        print("디렉토리가 아님")
else:
    print("존재X")
