n=int(input('number:'))
i=1
c=0
while i<=n:
    j=2
    while j<=n:
        if i%j==0:
            break
        j+=1
    if i==j:
        print(pc)
    i+=1
    


# n=int(input('number:'))
# i=1
# c=0
# while i<=n:
#     if n%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print('prime')
# else:
#     print('not')

# n=int(input('number:'))
# m=int(input('number:'))
# pc=0
# while n<m:
#     c=0
#     i=1
#     while i<=n:
#         if n%i==0:
#             c+=1
#         i+=1
#     if c==2:
#         pc=pc+1
#     n=n+1
# print(pc)