def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    l = len(s)
    if not s[:2].isalpha():
        return False
    s = list(s)
    if l > 6 or l < 2:
        return False
    while s:
        n = s.pop(0)
        if not n.isalnum():
            return False
        if not n.isalpha():
            if n == "0":
                return False
            else:
                while s:
                    n = s.pop(0)
                    if not n.isnumeric():
                        return False
    return True


main()
