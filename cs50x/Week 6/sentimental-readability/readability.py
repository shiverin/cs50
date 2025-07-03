from cs50 import get_string

text = get_string("Text: ")

word = 1
letter = 0
sentence = 0
for char in text:
    if char == " ":
        word += 1
    elif char == "." or char == "!" or char == "?":
        sentence += 1
    elif char.isalpha():
        letter += 1

L = (letter/word)*100
S = (sentence/word)*100

res = round(0.0588 * L - 0.296 * S - 15.8)
if res < 1:
    print("Before Grade 1")
elif res > 16:
    print("Grade 16+")
else:
    print(f"Grade {res}")
