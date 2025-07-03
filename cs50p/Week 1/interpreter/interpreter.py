x=input("hello").split()
a,b=float(x[0]),float(x[2])
if x[1]=="+":
    a+=b
elif x[1]=="-":
    a-=b
elif x[1]=="*":
    a*=b
elif x[1]=="/":
    a=a/b
print(a)
