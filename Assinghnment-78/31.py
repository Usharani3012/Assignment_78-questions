# Write a program that takes a number from the user and prints the number that is formed by reversing the digits of the number.
n=int(input('number:'))
r=0
while n>0:
    a=n%10
    r=r*10+a
    n=n//10
print(r)