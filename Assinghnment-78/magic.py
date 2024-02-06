l=[]
n=int(input('num:'))
for i in range(n):
    li=[0]*n
    l.append(li)
k=1
i=0
j=n//2
while k<=n*n:
    l[i][j]=k
    k=k+1
    nexti=(i-1)%n
    nextj=(j+1)%n
    if (l[nexti][nextj]):
        i+=1
    else:
        i=nexti
        j=nextj
print(l)