# x=int(input('number:'))
# n=int(input('number:'))
# i=1
# s=0
# while i<=n:
#     t=(x**i)/i
#     s=s+t
#     i+=1
#     print(s)

x=int(input('number:'))
n=int(input('number:'))
i=1
s=0
s1=0
c=1
while c<=n:
    t=i
    while t>0:
        if c%2==0:
            s1=(-1)*x**i/i
        else:
            s1=x**i/i
        s=s+s1
        i+=2
        c+=1
print(s)