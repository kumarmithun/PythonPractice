

import math

try:
    number = float(input("Enter a number: "))

    if number < 0:
        print("Square root and logarithm are not defined for negative numbers.")
    else:
        sqrt_result = math.sqrt(number)
        log_result = math.log(number)
        sine_result = math.sin(number)  # input is treated as radians

        print(f"Square root of {number}: {sqrt_result}")
        print(f"Natural logarithm of {number}: {log_result}")
        print(f"Sine of {number} (in radians): {sine_result}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
