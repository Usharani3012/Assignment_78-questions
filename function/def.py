# def greet():
#     print('hello')
# name=input()
# print(name)

# def greet():
#     print('hello')
# name=input()
# print(name)
# greet()

# def greet():
#     print('hello')
# greet()
# name=input()
# print(name)

# def greet():
#     print('hello')
# name=input()
# greet()
# print(name)

# def greet(word):
#     msg='hello'+word
#     print(msg)
# name=input()
# greet(word=name)


# def greet(word):
#     msg="hello"+word
#     return msg
#     print (msg)
# name=input()
# greetungs=greet(word=name)

# def greet():
#     msg='hello'
#     print(msg)
# print(print(greet()))

# def greet():
#     msg='hello'
#     print(msg)
# print(greet())

# l=[1,6,56,89,30,26,40,36]
# mn=int(input('num:'))
# mx=int(input('num'))
# c=0
# if l>=mn and l<=mx:
#     c+=1
#     print(i)

# power of 2

# def poweroftwo (n):
#     s=0
#     if n==0:
#         return 1
#     else:
#         power=poweroftwo(n-1)
#         return power*2
#     s=s+p
# n=int(input())
# print(poweroftwo(n))

# def fibinocies(n):
#     x=0
#     y=1
#     z=0
#     while z<=n:
#         x=y
#         y=z
#         z=x+y
# n=int(input('number:'))
# print(z)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact=factorial(n-1)
        return fact*n
n=int(input('number:'))
print(factorial(n))


