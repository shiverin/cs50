import sys

if len(sys.argv) != 2:
    print("no")
    sys.exit("no")
x = sys.argv[1]
if x[-2:] != "py":
    sys.exit("no")
r = 0
with open(x) as file:
    for line in file:
        line = line.strip()
        if line == "" or line[0] == "#":
            continue
        r += 1
print(r)
