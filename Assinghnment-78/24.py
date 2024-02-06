# Take a number N from the user as input, and print even numbers up to N.


n=int(input('num:'))
i=1
while i<n:
    if i%2==0:
        print(i,end='  ')
    i+=1