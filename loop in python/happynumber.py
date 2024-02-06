n=int(input(' '))
t=n
while t!=1 and t!=4:
    s=0
    while t>0:
      a=t%10
      s=s+a**2
      t=t//10
    t=s	
if s==1:
    print('happy')
else:
	 print('not')
   