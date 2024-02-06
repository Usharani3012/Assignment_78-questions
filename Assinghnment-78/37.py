# Write a program to take a number from the user and then determine if that number is a special type of number called a 'perfect number'.
n=int(input(''))
t=n
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
if t==s:
    print('perfect')
else:
    print('not')