def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if begin(s) and numbers(s) and length(s) and spec(s):
        return True
    else:
        return False

def begin(s):
    for charechter in s[:2]:

        if charechter.isdigit():
            return False
    return True

def numbers(s):
    firstnumber = None
    for charechter in s:

        if charechter.isdigit():
            firstnumber = charechter
            break

    if firstnumber == None:
        return True

    if int(firstnumber) == 0:
        return False

    index = s.index(firstnumber)
    position = len(s) - index

    for charechter in s[-position:]:
        if not charechter.isdigit():
            return False

    return True

def length(s):
    if not 2<= len(s) <= 6:
        return False
    else:
        return True

def spec(s):
    for charechter in s:

        if not charechter.isalpha() and not charechter.isdigit():
            return False
    return True

main()