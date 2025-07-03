month = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
while True:
    try:
        x = input("Date: ").strip()
        if "/" in x:
            a, b, c = x.split("/")
            if not int(a) in list(month.values()):
                continue
        elif "," in x:
            x = x.capitalize()
            x = x.replace(",", "")
            a, b, c = x.split()
            if a in month:
                a = month[a]
            else:
                continue
        else:
            continue
        if int(b) > 31:
            continue
        a = str(a).zfill(2)
        b = str(b).zfill(2)
        print(f"{c}-{a}-{b}")
        break
    except Exception:
        continue
