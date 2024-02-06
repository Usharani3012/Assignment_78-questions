# Write a program  to input electricity unit charges and calculate the total electricity bill according to the given condition:
# For the first 50 units Rs. 0.50/unit
# For the next 100 units Rs. 0.75/unit
# For the next 100 units Rs. 1.20/unit
# For units above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
u=int(input('units:'))
if u<=50:
	t=u*0.5
elif u<=100:
	t=u*0.75
elif u>100:
	t=u*1.20
elif u>=250:
	t=u*1.50
e=t*20/100
print(t+e)