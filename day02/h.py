s = set[int | str]()
s.add(1)
s.add("a")
s.add(2)
s.add(1)
s.update([4, 6, 7])
print(len(s))
s.add(9)
print(s)
print(s.pop())
# s.remove(123123)  # KeyError
s.discard(123123)  # OK
# s.clear()

for e in s:
    print(e)
