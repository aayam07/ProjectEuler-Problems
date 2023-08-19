# Problem - 20: Find the sum of digits in number 100!


# Function to find the factorial of a number
def find_factorial(num):
    factorial_result = 1
    for i in range(num, 0, -1):
        factorial_result *= i

    return factorial_result

# Function to calculate the sum of the digits in the factorial result number
def sum_of_digits(num):
    sum = 0
    num_as_str = str(num)
    for n in num_as_str:
        digit_as_int = int(n)
        sum += digit_as_int

    return sum


number = 100
factorial_result = find_factorial(number)
sum_of_factorial_result = sum_of_digits(factorial_result)

print(f"The sum of digits in {number}! = {sum_of_factorial_result}")

