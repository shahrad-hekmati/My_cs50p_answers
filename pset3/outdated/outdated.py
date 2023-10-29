months= [
    "January",
    "February",
    "March" ,
    "April" ,
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while True:
    date = input("date: ").strip()

    if "/" in date:
        mo, da, ye = date.split("/")

        if mo in months:
            mo = months.index(mo) + 1

        elif (int(da) > 0 and int(da) < 32) and (int(mo) > 0 and int(mo) < 13):
            break

    else:
        try:
            alternative_mo, alternative_da, ye = date.split(" ")

            if ye == "1636" and "," not in alternative_da:
                date = input("date: ").strip()

            if alternative_mo in months:
                mo = months.index(alternative_mo) + 1
                
            da = alternative_da.replace(",", "")
            if (int(da) > 0 and int(da) < 32) and (int(mo) > 0 and int(mo) < 13):
                break
        except:
            date = input("date: ").strip()

print(f"{ye}-{int(mo):02}-{int(da):02}")