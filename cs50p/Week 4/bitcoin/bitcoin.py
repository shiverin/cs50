import requests
import sys

while True:
    try:
        x=float(input("How many BTC u want buy??? "))
        break
    except ValueError:
        sys.exit("No")

url='http://rest.coincap.io/v3/assets/bitcoin?apiKey=910c034d0680b478f39d09ab7caf96a1c842dd1f2fb05651042534047960b8d0'

try:
    r=requests.get(url)
    d=r.json()
except requests.RequestException:
    sys.exit("No")

y=float(d["data"]["priceUsd"])
amount=x*float(y)
print(f"PRICE OF ONE BITCOIN NOW IS ${y:,.4f}")
print(f"TO PAY ${amount:,.4f}")

