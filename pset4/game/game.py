import random

level = -1
while level < 0:
    try:
        level = int(input("Level: "))
    except Exception:
        pass

random_num = int(random.randint(0, level))
guess = 0


while 1:
    try:
        guess = int(input("Guess: "))
        if guess > 0 and guess < level:
            if guess < random_num:
                print("Too small!")

            elif guess > random_num:
                print("Too large!")

            else:
                print("Just right!")
                break

    except Exception:
        pass
