#
# Task 2: Sum of Integers from 1 to 50 Using a Loop
#
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.


total_sum=0
for num in range(1, 50):
    #print(num)
    total_sum+= num
print("The sum of 1 to 50 is : " + str (total_sum))