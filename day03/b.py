try:
    with open("day03/b.txt", "r+b") as file:
        print(file)
        print(int(file.readline()))
except FileNotFoundError as e:
    print(e)
except (TypeError, ValueError) as e:
    print(e)
