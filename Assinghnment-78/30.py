# Write a program to input a number and check whether it is a perfect square or not.

# n=int(input('num:'))
# i=1
# a=0
# while i<=n:
#     a=i**i
#     i+=1
# if n==a:
#     print('perfect seq')
# else:
#     print('not')

n=int(input('num;'))
i=1
a=0
while a<n:
    a=i*i
    i+=1
if a==n:
    print('yes')
else:
    print('no')