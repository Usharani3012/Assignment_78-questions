n=int(input('number:'))
i=1
f=0
while i<=n:
    if n%i==0:
        f+=1
    i+=1
if f==2:
    print('prime')
else:
    print('not')