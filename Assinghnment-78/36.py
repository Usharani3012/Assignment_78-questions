n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
a=n1
b=n2
while b!=0:
    c=b
    b=a%b
    a=c
lcm=(n1*n2)//a
print("HCF of ",n1," and ",n2," is:",a)
print("LCM of ",n1," and ",n2," is:",lcm)