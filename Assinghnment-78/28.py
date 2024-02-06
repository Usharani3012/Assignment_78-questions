#Write a program to take a number from the user and print the number digits in the given number.

n=int(input('num:'))
c=0
while n>0:
    a=n%10
    c+=1
    n=n//10
print(c)