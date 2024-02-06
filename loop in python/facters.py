n=int(input('number:'))
i=1
while i<=n:
    c=0
    if n%i==0:
        j=1
        while j<=i:
            if i%j==0:
                c+=1
            j+=1
        if c==2:
            print(i)
    i+=1