# Problem - 2: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

num1 = 0
num2 = 1
fib_series_list = []

# to generate fibonacci series list upto 4 million
while True:
    next_num = num1 + num2
    num1 = num2
    num2 = next_num
    
    if (next_num > 4000000):
        break  # exit while loop

    fib_series_list.append(next_num)

# to find the sum of even numbers in the list
def sum_of_even_numbers():
    sum = 0
    for num in fib_series_list:
        if (num % 2 == 0):
            sum += num

    return sum

print(fib_series_list) 
print(sum_of_even_numbers())
        
