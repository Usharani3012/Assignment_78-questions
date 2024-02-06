# Write a program to take a year from the user and output whether a given year is a leap year or not.

y=int(input('year:'))
if y%4==0:
    if y%400==0:
        print('yes')
    elif y%100!=0:
        print('yes')
    else:
        print('no')
else:
    print('no')


# y=int(input('year:'))
# if y%400==0 or y%4==0 and y%100!=0:
#     print('leap year')
# else:
#     print('not')
    