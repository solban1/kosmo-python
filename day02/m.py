def f(b: str, *args: str, **kwargs: str) -> None:
    for i in args:
        print(i)
    print(kwargs["a"])


f("121241", "12321341", a="asdfasdf")


def g(*, a: str, b: str = "b") -> None:
    print(a)
    print(b)


g("a", "b")
