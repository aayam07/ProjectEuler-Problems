# Problem - 3: To find the largest prime factor of a given number

def largest_prime_factor(num):
    i = 2  # starting from 2 to check for factors
    while (i * i) <= num:  # consider factors upto square of number
        if (num % i != 0):
            i += 1  # increment the divisor by 1 when the number is not divisible
        else:
            num = num // i  # floor of the num divided by i

    return num

result = largest_prime_factor(600851475143)
print(result)




    
