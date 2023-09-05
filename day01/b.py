# variables
a = 100  # int
b = "str"  # str

c, d = "짜장", "짬뽕"
c, d = d, c
print(c)

e, f, g = "마라탕"
print(f)  # "라"

h = i = j = "탕수육"
print(i)  # "탕수육"


class MyClass:
    def __init__(self, name) -> None:
        self.name = name


print(MyClass("강감찬").name)
