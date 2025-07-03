def main():
    x=input("Time").strip().lower()
    x=convert(x)
    if 7<=x<=8:
        print("Breakfast Time")
    elif 12<=x<=13:
        print("Lunch Time")
    elif 18<=x<=19:
        print("Dinner Time")
def convert(time):
    time=list(time)
    h=""
    m=""
    while time:
        c=time.pop(0)
        if c==":":
            break
        else:
            h+=c
    while time:
        m+=time.pop(0)
    return float(h)+(float(m)/60)

if __name__ == "__main__":
    main()
