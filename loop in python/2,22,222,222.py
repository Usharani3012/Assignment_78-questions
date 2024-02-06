# n=int(input('number'))
# b='2'
# i=0
# while i < n:
#     print(b,end=' ')
#     i+=1
#     b+='2'


# n=int(input('number:'))
# a='2'
# for i in range(n):
#     print(a,end=" ")
#     a=a+"2"

#sum of same series......
n=int(input('number'))
b='2'
i=0
s=0
while i < n:
    s=s+b
    i+=1
    b+='2'
print(s)