import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        "([1][0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to ([1][0-2]|[1-9])(:[0-5][0-9])? (AM|PM)", s)
    if not match:
        raise ValueError("no")
    else:
        a, b, c, d, e, f = match.groups()
        if c == "PM":
            a = int(a)
            if a==12:
                a=0
            a += 12
        else:
            if int(a)==12:
                a="00"
            elif int(a)<10:
                a="0"+a
        if b == None:
            b = "00"
        else:
            b = b[1:]
        if f == "PM":
            d = int(d)
            if d==12:
                d=0
            d += 12
        else:
            if int(d)==12:
                d="00"
            elif int(d)<10:
                d="0"+d
        if e == None:
            e = "00"
        else:
            e = e[1:]
        return f"{a}:{b} to {d}:{e}"


if __name__ == "__main__":
    main()
"""
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
"""
