# Problem - 10: Find the sum of all the primes below two million.

sum = 5  # considering 2 and 3 as first two prime numbers. So, 2 + 3 = 5

# checking all the prime numbers from 4 to two million
for n in range(4, 2000000):
    flag = False  # initialize flag for each number
    for i in range(2, int(n ** 0.5)+1):  # check upto the square root of the number. Works for (number > 3).
        if (n % i == 0):
            flag = True  # composite
            break  

    if not flag:  # prime
        sum += n  # add the prime number to the sum

print(f"Sum of prime numbers below two million is: {sum}")


