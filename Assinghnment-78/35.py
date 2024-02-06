# Write a program to check if a number is a special type of number called a 'prime number'. A prime number is a number that is only divisible by 1 and itself, and it doesn't have any other factors. 
# For example, the number 7 is a prime number because it can only be divided by 1 and 7 without leaving a remainder. However, the number 12 is not a prime number because it has other factors, such as 2, 3, 4, and 6, in addition to 1 and 12. (Take the number from the user)?

n=int(input('num:'))
i=1
while i<=n:
    if n%i==0: 
        print(i)
    i+=1
    t=1
    c=0
    while t>0:
        if i%t==0:
            c+=1
    print(t)
else:
    print('not')
    