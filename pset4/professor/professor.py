import random

def main():
    equal_number = 10
    score = 0
    chances = 3
    lvl = get_level()
    while equal_number != 0:
        if chances == 3:
            element1, element2 = generate_integer(lvl)

        try:
            user_answer = int(input(f"{element1} + {element2} = "))
            answer = element1 + element2
            if user_answer == answer:
                equal_number = equal_number - 1
                score += 1
                chances = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            chances -= 1
            pass
        if chances == 0:
            print((f"{element1} + {element2} = {answer}"))
            chances = 3
            equal_number -= 1
            continue
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass


def generate_integer(level):
    if level == 1:
        element1 = random.randint(0, 9)
        element2 = random.randint(0, 9)

    elif level == 2:
        element1 = random.randint(10, 99)
        element2 = random.randint(10, 99)

    elif level == 3:
        element1 = random.randint(100, 999)
        element2 = random.randint(100, 999)

    return element1, element2


if __name__ == "__main__":
    main()