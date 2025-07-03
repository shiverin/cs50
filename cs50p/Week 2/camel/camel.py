x = input("camelCase: ").strip()
x = list(x)
r = ""
while x:
    z = x.pop(0)
    if z.isupper():
        r += "_"
    z = z.lower()
    r += z
print(r)
