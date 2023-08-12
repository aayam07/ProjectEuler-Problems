# Problem - 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
import math

numbers = list(range(1, 21))  # list of all the numbers from 1 to 20
result = math.lcm(*numbers)

# print(numbers)
print(f"The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {result}")
