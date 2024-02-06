# Write a program to take 3 numbers from the user and output the second max of 3 numbers.
# (First, do it in the normal way then do it by using 3 comparisons)
a=int(input('number:'))
b=int(input('number:'))
c=int(input('number:'))
if a>b:
    if a<c:
        print(a)    
else: 
    if a<b:
        if a>c:     
            print(a)
if b>a:    
    if b<c:   
        print(b)
else:
    if b<a:    
        if b>c:   
            print(b) 
if c>a:
    if c<b:
        print(c)
else:
    if c<a:    
        if c>b:   
                print(c)
                
                
# a=int(input('number:'))
# b=int(input('number:'))
# c=int(input('number:')) 
# if a>b and a<c or a<b and a>c:   
#     print(a)
# elif b>a and b<c or b<a and b>c:    
#     print(b)
# else:
#     print(c)              