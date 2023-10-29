def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    converted = float(d.replace("$", ""))
    return converted

def percent_to_float(p):
    converted = float(p.replace("%", ""))
    return converted / 100
main()