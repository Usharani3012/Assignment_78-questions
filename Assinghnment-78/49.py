# Write a program to take a number and print the count of the prime numbers that are strictly less than a number.

n=int(input('number:'))
m=int(input('number:'))
pc=0
while n<m:
    c=0
    i=1
    while i<=n:
        if n%i==0:
            c+=1
        i+=1
    if c==2:
        pc=pc+1
    n=n+1
print(pc)
