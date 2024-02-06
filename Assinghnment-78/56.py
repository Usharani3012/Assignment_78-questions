a=int(input('enter the num: '))
l=[]
i=0
while i<a:   
    b=int(input("enterr the num in list:"))
    l.append(b)
    i=i+1
s=0
s1=0
i=0
while i<len(l):
    if l[i]%2==0:
        s=s+l[i]
    else:
        s1+=l[i]
    i=i+1
print('even numbers:',s)
print('odd numbers:',s1)