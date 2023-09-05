d: dict[str, int | str] = {}
d["name"] = "foo"
d["age"] = "bar"

for k, v in d.items():
    print(k, v)


if "foo" in d.values():
    print("foo")

d.update({"name": "baz", "addr": "NY"})
print(d)

d = {"name": "bbb", "height": "123", **d}
print(d)

e = {}

for k, v in d.items():  # (('name', 'baz'), ('height', '123'), ...)
    e[k] = v


x = [10, 20, 30]
y = [100, 200, 300]
for i in x:
    i = i + 5
    print(i)
