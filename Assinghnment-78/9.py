# Write a program to take two numbers, A and B from the user. Your task is to find the largest number that is less than A and can be divided evenly by B. Can you figure out that number?
a=int(input('number:'))
b=int(input('number:'))
t=a%b
print(b*t)