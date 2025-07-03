
while True:
    x = list(input("fraction: "))
    a = ""
    b = ""
    s = False
    try:
        while x:
            n = x.pop(0)
            if n == "/":
                s = True
                continue
            if not s:
                a += n
            else:
                b += n
        r = (float(int(a))/float(int(b)))
        if r > 1:
            continue
        break
    except (ValueError, ZeroDivisionError):
        pass

r = round((r)*100)
if r >= 99:
    print("F")
elif r <= 1:
    print("E")
else:
    print(f"{r}%")
