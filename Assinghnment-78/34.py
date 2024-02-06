# Write a program to take a number from the user and print all the factors of the given number. A factor is a number that can divide another number evenly without leaving a remainder
n=int(input('num:'))
i=1
while i<=n:
    if n%i==0: 
        print(i)
    i+=1