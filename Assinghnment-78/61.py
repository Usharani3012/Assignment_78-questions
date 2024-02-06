 
 	
# Write a program to take N numbers from a user as input and then print the duplicates in those N numbers. Also, take N as an input from the user.


n=int(input('num:'))
l=list(map(int,input('list:').split()))
i=0
a=[]
while i<n:
    j=0
    c=0
    while j<n:
        if l[i]==l[j]:
            c=c+1
        j+=1
    if l[i] not in a:
        a.append(l[i])
        print(l[i],c)
    i+=1 
        