#mathemeatical Operations

num1= int(input("Enter the First Number:"))
num2= int(input("Enter the Second Number:"))

addition = num1 + num2
print("Addition:" + str(addition) )

substraction = num1 - num2
print("Substraction:" + str(substraction) )

Multiplication = num1 * num2
print("Multiplication:" + str(Multiplication) )

Divide = num1 / num2
print("Divide:" + str(Divide) )



# Task 2: Create a Personalized Greeting
# Problem Statement: Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

fname = str(input("Enter the First Name:"))
lname = str(input("Enter the Last Name:"))
cname = str(fname+lname)
greeting = print("Hello " +cname+ "! Welcome to the Python Programming")
