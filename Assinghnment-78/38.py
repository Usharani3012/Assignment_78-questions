# arm strong number or not..........

n=int(input(''))
t=n
l=len(str(n))
s=0
while n>0:
    a=n%10
    s=s+a**l
    n=n//10
if t==s:
    print('arm')
else:
    print('not')