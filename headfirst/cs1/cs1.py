#!/usr/bin/env python3
import constant
print("In the first lession of python tutorial. We'll learn about: \n" \
        "1. Variables\n" \
        "2. Datatypes\n" \
        "3. Operaters\n" \
)

print("1.Variables\n")
# In python constants are usually declared and assigned on a module
firstName = 'Son' # string
lastName = "Nguyen" # string
age = 32 # integer
averageSalary = float(26000000) / float(constant.USD_TO_VND) # float

print( "Fullname: " + firstName + " " + lastName + '\n' + \
       "Age: " + str(age) + '\n' + \
       "Average Salary: " + str(averageSalary) + "\n" )

print( "Fullname: %s %s\n" % (firstName, lastName) + \
        "Age: %d\n" % age + \
        "Average Salary: %0.2f USD/month" % round(averageSalary, 2))
print("-"*100)
print((
       "Fullname: {firstName} {lastName}\n" + \
       "Age: {age}\n" + \
       "Average Salary: {averageSalary}\n") \
       .format(firstName=firstName, lastName=lastName, age=age, averageSalary=averageSalary) )

print("Fullname: {}".format(firstName + lastName))
