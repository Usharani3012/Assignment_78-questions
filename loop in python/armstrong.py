# arm strong number or not..........

n=int(input(''))
t=n
l=len(str(n))
s=0
while n>0:
    a=n%10
    s=s+a**l
    n=n//10
    print(s)
if t==s:
    print('arm')
else:
    print('not')  


#count of armstrong numbrs........

# n=int(input('number:'))
# m=int(input('number:'))
# c=0
# while n<=m:
#     l=len(str(n))
#     s=0
#     t=n
#     while t>0:
#         a=t%10
#         s=s+a**l
#         t=t//10
#     if n==s:
#         c=c+1
#         print(s,end=' ')
#     n+=1
# print()
# print("the count of the numbers:",c)
    
        
    
