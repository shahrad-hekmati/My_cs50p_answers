import sys
import inflect

x = inflect.engine()
names = []

while True:
    try:
        str_input = input("Name: ").title()
        if len(str_input) < 1:
            sys.exit(0)

        names.append(str_input)

    except EOFError:
        print(f"\nAdieu, adieu, to {x.join(names)}")
        break