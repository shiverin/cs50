from datetime import date, datetime
import re
import sys
import inflect


def main():
    x = input("your bday: ")
    verify(x)
    x = datetime.strptime(x, "%Y-%m-%d").date()
    y = date.today()
    a = y-x
    m = (a.days)*24*60
    p = inflect.engine()
    p = p.number_to_words(m).capitalize()
    p = p.replace(" and", "")
    print(p+" minutes")


def verify(x):
    match = re.search(r"^\d{4}-([1][0-2]|[0][1-9])-([0][1-9]|[1-2][0-9]|[3][0-1])$", x)
    if match == None:
        sys.exit("no")
    else:
        return True


if __name__ == "__main__":
    main()
