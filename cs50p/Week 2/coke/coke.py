y = [25, 10, 5]
p = 50
while p > 0:
    x = int(input("Insert Coin: "))
    if x in y:
        p -= x
    if p <= 0:
        print(f"Change Owed: {-p}")
    else:
        print(f"Amount Due: {p}")
