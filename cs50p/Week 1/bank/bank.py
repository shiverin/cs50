x=input("Greeting: ")
x=x.split()
x=x[0].lower()
if x.startswith("hello"):
        print("$0")
elif x[0]=="h":
    print("$20")
else:
    print("$100")
