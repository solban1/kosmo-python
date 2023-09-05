a1 = [1, 2, 3]
a2 = a1.copy()  # shallow copy
a2[0] = 3
print(a1)
print(a2)
print(a1 is a2)  # False

a3 = [1, 2, 3]
a4 = a3  # assign reference
a4[0] = 3
print(a3)
print(a4)
print(a3 is a4)  # True
