# Problem - 1: To find the sum of all the multiples of 3 or 5 below 1000


def sum_of_multitples():
    sum = 0
    for num in range(1, 1000):
        if (num % 3) == 0 or (num % 5) == 0:
            sum += num 

    return sum

print(sum_of_multitples())