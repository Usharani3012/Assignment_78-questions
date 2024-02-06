n=int(input('number:'))
t=n
while n>9:
    s=0
    while n>0:
        a=n%10
        s=s+a
        n=n//10
    n=s
if s==1:
    print('magic')
else:
    print('not')