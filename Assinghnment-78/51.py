n=int(input('number'))
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
    b=0
    t=s
    while t>0:
        c=t%10
        b=b+c
        t=t//10
print(b)
        

