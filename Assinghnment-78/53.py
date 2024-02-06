n=int(input('enter the num;'))
i=1
t=[]
while i<=n:
    a=int(input('num:'))
    t.append(a)
    i+=1
print(t)
d=int(input('delet position:'))
i=0
while i<len(t):
    if i==d-1:  
        t.delete(t[i]) 
    else:
         
    i+=1
print(t)
        

    