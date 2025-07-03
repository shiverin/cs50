def main():
    x=input()
    print(f"${value(x)}")

def value(greeting):
    x=greeting.split()
    x=x[0].lower()
    if x.startswith("hello"):
            return(0)
    elif x[0]=="h":
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()
