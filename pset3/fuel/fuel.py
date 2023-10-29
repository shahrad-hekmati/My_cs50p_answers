def check_vals(el1, el2):

    if el1 == 0 and el2 == 100:
            print("E")
    elif el1 == 1 and el2 == 100:
            print("E")

    elif el1 == 100 and el2 == 100:
            print("F")

    elif el1 == 99 and el2 == 100:
            print("F")

    elif el2 < el1 or el2 == 0:
         raise ValueError

    else:
        print(f"{round((el1 / el2) * 100)}%")

try:
    fraction = input("Fraction: ")

    try:
        el1, el2 = fraction.split("/")
        el1 = int(el1)
        el2 = int(el2)
        check_vals(el1, el2)

    except:
        fraction = input("Fraction: ")
except:
      pass