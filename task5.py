#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
import math

nums = (5,-2,12,-8,14,16)

for i in nums:
    if i % 2 == 0:
        squareroot = math.sqrt(i)
        print(f"{i} and the square root is {squareroot}")
    else:
        continue
