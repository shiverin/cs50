from cs50 import get_int

while True:
    height = get_int("height: ")
    if height > 0 and height < 9:
        break

for i in range(1, height+1):
    print(f"{" "*(height-i)}{"#"*i}{" "*2}{"#"*i}")
