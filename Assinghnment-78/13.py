#  Write a program to take an integer as input and print the smallest positive integer that is a multiple of both 2 and n.
n=int(input('number:'))
if n%2==0 and n%n==0:
    print(n)
else:
    print(n*2)