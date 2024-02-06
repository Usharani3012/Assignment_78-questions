 # Write a program that rotates the elements of a list so that the elements at the first index move to the second elements at the second index move to the third and so on. The last element moves at the first index. (Take array and no_of_rotations from the user)




n=int(input('num:'))
l=list(map(int,input('enter the num:').split()))
k=int(input('rotation valve:'))
t=0
i=1
while i<=k:
    t=l[0]
    j=0
    while j<n-1:
        l[j]=l[j+1]
        j+=1
    l[j]=t
    i+=1
print(l)
        