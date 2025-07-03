r="Adieu, adieu, to"
n=0
temp=""
while True:
    try:
        x=input("")
        if n==1:
            r+=" "
        if n>=1:
            r+=temp+", "
        elif n==0:
            r+=temp
            curr=x
        temp=x
        n+=1
    except EOFError:
        if n==0:
            pass
        if n==1:
            r+=" "+temp
        else:
            r+="and "+temp
        break
if n == 2:
    r = r.replace(", and", " and")
print(r)
