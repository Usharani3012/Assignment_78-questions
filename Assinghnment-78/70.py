#  Write aprogram to take a sorted array from the user as input and find a number using the Binary Search algo

# n=int(input('num:'))
# l=list(map(int,input('enter the num:').split()))
# k=int(input('num'))
# i=0
# while i<=n:
#     if l[i]==k:
#         print('yes')
#     else:
#         print('no')
#     i+=1


n=int(input('number:'))
i=0
t=[]
while i<=n:
    e=int(input('list of elements:'))
    t.append(e)
    i+=1
t.sort()
g=int(input('guss num'))
l=0
r=len(t)-1
p='notin'
while l<=r:
    m=(l+r)//2
    c=t[m]
    if c==g:
        p=(t[m])
        break
    elif c<g:
        l=m+1
    else:
        r=m-1
print(p)
        
        



    
