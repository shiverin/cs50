import re
import sys


def main():
    x=input("IPv4 Address: ")
    print(validate(x))

def validate(ip):
    match=re.search("^(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|25[0-5]|2[0-4][0-9])\.(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|25[0-5]|2[0-4][0-9])\.(0|[1-9]|[1-9][0-9]|1[0-9][0-0]|25[0-5]|2[0-4][0-9])\.(0|[1-9]|[1-9][0-9]|1[0-9][0-9]|25[0-5]|2[0-4][0-9])$",ip)
    return match!=None



if __name__ == "__main__":
    main()
