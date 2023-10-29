import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    if match:
        from_time = standard_time(match.group(1), match.group(2), match.group(3))
        time = standard_time(match.group(4), match.group(5), match.group(6))
        return f"{from_time} to {time}"
    else:
        raise ValueError

def standard_time(h, m, x):
    if h == "12":
        if x == "AM":
            hour = "00"
        else:
            hour = "12"
    else:
        if x == "AM":
            hour = f"{int(h):02}"
        else:
            hour = f"{int(h)+12}"
    if m == None:
        minute = "00"
    else:
        minute = f"{int(m):02}"
    return f"{hour}:{minute}"


if __name__ == "__main__":
    main()