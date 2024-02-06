n=int(input('number:'))
c=0
while n>0:
    if n%10==0:
        c+=1
    n=n//10
if c>=1:
    print('duck number')
else:
    print('not')