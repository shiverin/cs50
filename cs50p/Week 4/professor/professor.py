import random


def main():
    x = get_level()
    s = 0
    for n in range(10):
        a = generate_integer(x)
        b = generate_integer(x)
        for i in range(3):
            try:
                y = int(input(f"{a} + {b} = "))
                if y == a+b:
                    s += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{a} + {b} = {a+b}")

    print(f"{s}")


def get_level():
    while True:
        try:
            r = int(input(""))
            if not 1 <= r <= 3:
                continue
            else:
                break
        except ValueError:
            pass
    return r


def generate_integer(level):
    if level == 1:
        return (random.randint((10**(level-1)-1), (10**(level)-1)))
    else:
        return (random.randint((10**(level-1)), (10**(level)-1)))


if __name__ == "__main__":
    main()
