def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(given_val):
    if 2 <= len(given_val) <= 6 and given_val.isalnum():

        if given_val.isalpha():
            return True
        else:
            if given_val[:2].isalpha() and given_val[-2:].isdigit():
                for i in range(len(given_val)):
                    if given_val[i].isdigit():

                        if given_val[i].startswith("0") or given_val[i:].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False


if __name__ == "__main__":
    main()