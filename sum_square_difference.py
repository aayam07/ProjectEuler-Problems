# Problem - 6: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares():
    sum = 0
    for n in range(1, 101):
        sum += (n * n)

    return sum

def square_of_sum():
    sum = 0
    for n in range(1, 101):
        sum += n
    
    return (sum * sum)

value_sum_of_squares = sum_of_squares()
value_square_of_sum = square_of_sum()
difference = value_square_of_sum - value_sum_of_squares
print(f"The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {difference}")