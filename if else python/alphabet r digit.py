# a=input()
# if 'A'<= a <='Z':
# 	print('Alphabet')
# elif 'a'<= a <='z':
# 	print('Alphabet')
# elif '0'<= a <='9':
# 	print('number')
# else:
# 	print('special charecter')
	
# c=input()
# if c.isalpha():
# 	print('Alphabet')
# elif c.isdigit():
# 	print('Number')
# else:
# 	print('special char')

c=input()
if c>='A' and c<='Z' or c>='a' and c<='z':
	print('alphabet')
elif c>='0' and c<='9':
	print('Number')
else:
	print('special char')