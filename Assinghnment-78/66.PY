n=int(input('number'))
l1=list(map(int,input('list1:').split()))
l2=list(map(int,input('list2:').split()))
i=0
u=[]
inter=[]
while i<n:
    if l1[0]==l2[0]:
        inter.append(l1[i])
    else:
        u.append(l1())