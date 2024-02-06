n=int(input('number:'))
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
if n%s==0:
    print('harshad')
else:
    print('not')