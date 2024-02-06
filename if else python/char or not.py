# c=input( )
# if c.isalpha():
# 	print('alphabet')
# elif c.isdigit():
# 	print('not')

	
c = input("Enter a value: ")

if 'a' <= c <= 'z':
    print("The input is a char.")
else:
    print("The input is a digit.")