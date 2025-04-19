
# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.


num = int(input("Enter the Number:"))

if  num%2==0:
    print(str(num) + ": is Even Number")

else:
    print(str(num )+ ": is Odd Number")