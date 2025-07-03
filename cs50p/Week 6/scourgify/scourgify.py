import sys
import csv


if len(sys.argv) != 3:
    sys.exit("no")
x = sys.argv[1]
if not x.endswith(".csv"):
    sys.exit(1)
y = sys.argv[2]
if not y.endswith(".csv"):
    sys.exit("no")

try:
    with open(x, "r") as infile, open(y, "w", newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ["first", "last", "house"]  # add new ones
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            full = row["name"].split(",")
            first = full[0].strip()
            last = full[1].strip()
            temp = {
                "first": last,
                "last": first,
                "house": row.get("house", "")
            }
            writer.writerow(temp)
except FileNotFoundError:
    sys.exit(2)
