# Write a program to take the basic salary of an employee and calculate its Gross salary according to the following: (Gross salary is the sum of basic salary, HRA, and DRA)
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%
bs=int(input('salary:'))
if bs<=10000:
	hr=(bs*20/100)
	da=(bs*80/100)
elif bs<=20000:
	hr=(bs*25/100)
	da=(bs*90/100)
elif bs>20000:
	hr=(bs*30/100)
	da=(bs*95/100)
gross_salary=bs+hr+da
print(gross_salary)