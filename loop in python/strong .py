n= int(input('number:'))
t=n
s=0
while n>0:
    f=1
    a=n%10
    while a>0:
        f=f*a
        a-=1
    s=s+f
    n=n//10
if t==s:
    print('strong')
else:
    print('not')
        