'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

# open the file

infile = open('employee_data.csv', 'r')

new_dict = {}
emp_name = []
emp_salary = []
emp_newsal = []

count = 1
for i in infile.readlines():
    i = i.split(',')
    if count == 1:
        emp_salary = []
        count += 1
    else:
        emp_name.append(f"{i[1]+ ' ' + i[2]}")
        emp_salary.append(f"{i[5]}")
        sal = i[5]
        new_sal = int(sal) * 1.1
        emp_newsal.append(round(new_sal, 2))
        count += 1

for i in range(len(emp_name)):
    new_dict[emp_name[i]] = emp_newsal[i]

print(new_dict)


for i in range(len(emp_name)):
    print(f"Employee Name: {emp_name[i]} Current Salary: ${emp_salary[i]}")

print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per image

for key, value in new_dict.items():
    print(f"Employee Name: {key} New Salary: ${value}")

print()
print('=========================================')
print()

# print out the total difference between the old salary and the new salary as per image.

count_sal = 0
count_newsal = 0

for i in range(len(emp_salary)):
    old_sal = int(emp_salary[i])
    count_sal += old_sal

for i in range(len(emp_newsal)):
    new_sal = int(emp_newsal[i])
    count_newsal += new_sal

inc_sal = count_newsal - count_sal

print(f"Total increase in salary: ${round(inc_sal,2)}")
