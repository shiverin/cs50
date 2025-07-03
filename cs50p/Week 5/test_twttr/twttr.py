
def main():
    x = input("Input: ")
    r=shorten(x)
    print(f"Output: {r}")
def shorten(word):
    word = list(word)
    v = ["A", "E", "I", "O", "U"]
    r = ""
    for n in word:
        if n.upper() in v:
            continue
        else:
            r += n
    return r


if __name__ == "__main__":
    main()
