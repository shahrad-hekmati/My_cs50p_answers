import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])


def clean(input, output):
    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(output, "w") as output:
                elements = ["first", "last", "house"]
                writer_for_csv = csv.DictWriter(output, fieldnames = elements)
                writer_for_csv.writeheader()
                for person in reader:
                    last, first = person["name"].split(", ")
                    house = person["house"]
                    writer_for_csv.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()