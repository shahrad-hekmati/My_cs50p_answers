from datetime import date
import inflect
import sys
import operator

inflect_eng = inflect.engine()

def main():
    try:
        dob = input("Date of Birth: ")
        differ = operator.sub(date.today(), date.fromisoformat(dob))
        print(convert(differ.days))
    except ValueError:
        sys.exit("Invalid date")

def convert(time):
    minutes = time * 24 * 60
    return f"{(inflect_eng.number_to_words(minutes, andword='')).capitalize()} minutes"

if __name__ == "__main__":
    main()