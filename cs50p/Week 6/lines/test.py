a="hi"
b="bye"

if len(b)>len(a):
    a,b=b,a

for n in range(len(a)):
    x=a[n]
    if n<len(b):
        y=b[n]
    else:
        y=" "
    print(f"{x} {y}")
