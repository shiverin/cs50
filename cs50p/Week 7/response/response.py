import validators


if (validators.email(input("Email")))==True:
    print("Valid")
else:
    print("Invalid")
