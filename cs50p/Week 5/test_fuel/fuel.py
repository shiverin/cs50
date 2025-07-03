def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except:
            pass  # keep prompting until valid input

def convert(fraction):
    try:
        num, denom = fraction.split("/")
        num = int(num)
        denom = int(denom)
        if denom == 0 or num > denom:
            raise ValueError
        return round((num / denom) * 100)
    except (ValueError, ZeroDivisionError):
        raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

