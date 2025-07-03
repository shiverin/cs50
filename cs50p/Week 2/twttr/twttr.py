x = input("Input: ")
x = list(x)
v = ["A", "E", "I", "O", "U"]
r = ""
for n in x:
    if n.upper() in v:
        continue
    else:
        r += n
print(f"Output: {r}")
