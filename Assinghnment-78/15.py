# # Write a program to take four numbers from the user and print the greater number of the four numbers. (assume all the numbers are distinct).
# a=int(input('number:'))
# b=int(input('number:'))
# c=int(input('number:'))
# d=int(input('number:'))
# if a>b:
#     if a>c:
#         if a>d:  
#             print(a)       
#         else:
#             print(d)
#     else:
#         print(c)
# else:
#     print(b)
    
    
# a=int(input('number:'))
# b=int(input('number:'))
# c=int(input('number:'))
# if a>b:
#     max1=a
#     smax1=b
# else:
#     max1=b
#     smax1=a
# if max1>c:
#     if c>smax1:
#         print (c) 
#     else:
#         print (smax1)
# else:
#     print (max1)
    
    
a=int(input('number:'))
b=int(input('number:'))
c=int(input('number:'))
d=int(input('number:'))
if a>b:
    max1=a
    smax1=b
else:
    max1=b
    smax1=a
if c>d:
    max2=c
    smax2=d
else:
    max2=d
    smax2=c
if max1>max2:
    if max1>smax1:
        print(max1)
    else:
        print(smax1)
else:
    if max1>smax2:
        print(max1)
    else:
        print(smax2)
       
    
    