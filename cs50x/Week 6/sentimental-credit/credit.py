from cs50 import get_string

card = get_string("Number: ")


def check(card):
    res = ""
    final = 0
    for char in card[-2::-2]:
        res += str(int(char)*2)
    for char in res:
        final += int(char)
    for char in card[-1::-2]:
        final += int(char)
    if final % 10 == 0:
        return True
    else:
        return False


if check(card) == True and len(card) == 15 and (card[0:2] == "34" or card[0:2] == "37"):
    print("AMEX")
elif check(card) == True and len(card) == 16 and (card[0:2] == "51" or card[0:2] == "52" or card[0:2] == "53" or card[0:2] == "54" or card[0:2] == "55"):
    print("MASTERCARD")
elif check(card) == True and (len(card) == 13 or len(card) == 16) and card[0] == "4":
    print("VISA")
else:
    print("INVALID")
