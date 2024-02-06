# Write a program to print the sum of odd numbers up to N
n=int(input('num:'))
i=1
s=0
while i<=n:
    if i%2!=0:
        s=s+i
    i+=1
print(s)
    