# slicing in list sting......

# names=['sandhya','usha','balu','hari']
# print(names)
# print(names[0:])
# print(names[2:])
# print(names[::-1])
# print(names[2:4])

# 1 fron start,5 is from stop and 2 is step

# number=[1,2,3,4,5,6,7,8,9,10]
# print(number)
# print(number[0:])
# print(number[::-1])
# print(number[1:5:2])
#print(number[:5])
# initializing list
test_list = ['n','i','t','i','n']
# Reversing the list
reverse = test_list[::-1]
# checking if palindrome
res = test_list == reverse
# printing result
if(res):
	print("Haan! palindrome hai")
else:
	print("Nahi! palindrome nahi h")

