n=int(input('number:'))
t=n
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
if t==r:
    print('polindrom')
else:
    print('no')