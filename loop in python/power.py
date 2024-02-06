n=int(input('number:'))
i=1
a=0
while a<n:
    a=2**i
    if a<=n:
        i=i+1 
print(2**(i-1))