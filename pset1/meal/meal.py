def main():
    time = input("What time is it? ").strip()
    ctime = convert(time)

    if 7.0 <= ctime <= 8.0:
        print("breakfast time")

    elif 12.0 <= ctime <= 13.0:
        print("lunch time")

    elif 18.0 <= ctime <= 19.0:
        print("dinner time")

def convert(time):
    if "a.m." in time or "p.m." in time:
        h_and_m, am_and_pm = time.split(" ")
        h_m = h_and_m.split(":")
        if am_and_pm == "p.m." and int(h_m[0]) < 12:
            h_m[0] = int(h_m[0])
            h_m[0] += 12
    else:
        h_m = time.split(":")

    return float(int(h_m[0]) + (int(h_m[1])/60))

if __name__ == "__main__":
    main()