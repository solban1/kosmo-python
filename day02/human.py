"""human.py"""


class Human:
    def __init__(self, name="홍길동"):
        self._name = name

    def say(self, dialog):
        print(f"{self._name}: {dialog}")

    def move(self):
        print(f"{self._name}(이)가 걷는다.")


class Superman(Human):
    def __init__(self, name="클락", power=100):
        super().__init__(name)
        self._power = power

    def move(self):
        print(f"{self._name}이(가) 날아간다.")

    def attack(self):
        print(f"{self._name}이(가) {self._power}의 힘으로 광선을 쏜다.")


kang = Human("강감찬")
kang.say("안녕")
kang.move()

clark = Superman(power=1000)
clark.move()
clark.say("하하")
clark.attack()
