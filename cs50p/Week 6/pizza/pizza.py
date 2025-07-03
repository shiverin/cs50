from tabulate import tabulate
import sys


if len(sys.argv)!=2:
    sys.exit("no")
x=sys.argv[1]
if not x.endswith(".csv"):
    sys.exit("no")

try:
    with open(x) as file:
        table=[]
        for line in file:
            line=line.strip().split(",")
            table.append(line)
        headers=table[0]
        table=table[1:]
    print(tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("no")

