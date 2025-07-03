r = {}

while True:
    try:
        x = input("item").upper()
        if x in r:
            r[x] += 1
        else:
            r[x] = 1
    except EOFError:
        r={i:r[i] for i in sorted(r.keys())}
        for n in r:
            print(f"{r[n]} {n}")
        break
