#Write a program to take a number from the user and print the sum of the digits of the given number.

n=int(input('number:'))
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
print(s)