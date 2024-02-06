# Write a program to take 4 numbers from the user and output the second max of these 4 numbers
a=int(input('number:'))
b=int(input('number:'))
c=int(input('number:'))
d=int(input('number:'))
if a>b:    
    if a<c:   
        if a<d:   
            print(a)
elif a<b:       
    if a>c:         
        if a<d:       
            print(a)   
else:
    if a<b:
        if a<c:    
            if a>d:    
                print(a)