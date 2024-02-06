# Write a program to take two integers M, and N and print the sum of numbers in the range M to N.
m=int(input('num:'))
n=int(input('num:'))
i=m
s=0 
while i<=n:
    s=s+i
    i+=1
print(s)

    