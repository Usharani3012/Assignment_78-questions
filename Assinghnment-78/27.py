# Write a program to calculate the sum of the following series where N is input from the user. 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/N
n=int(input('number:'))
i=1
t=i
s=0
while i<=n:
    a=t/i
    s=s+a
    i+=1
print(s)