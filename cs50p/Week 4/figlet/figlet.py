from pyfiglet import Figlet
import sys

if not len(sys.argv)==3:
        sys.exit("no")
if not sys.argv[1]=="-f" or sys.argv[1]=="--font":
        sys.exit("no")
f=sys.argv[2]
x=input("Input: ")
hi=Figlet()
hi.setFont(font=f)
print(hi.renderText(x))
