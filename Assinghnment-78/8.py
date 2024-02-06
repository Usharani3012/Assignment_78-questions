# Write a program to take two inputs from the user and swap them without using a temporary or third variable.

a=int(input('number:'))
b=int(input('number:'))
a,b=b,a
print(a)
print(b)