# Problem - 8: There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
# a < b < c where a^2 + b^2 = c^2

def find_pythagorean_triplet(sum_value):
    for a in range(1, sum_value):
        for b in range(a+1, sum_value - 1):
            c = sum_value - a - b  # calculate the value of c
            if (a ** 2 + b ** 2 == c ** 2):
                return a, b, c

sum_value = 1000
a, b, c = find_pythagorean_triplet(sum_value)
print(f"The product of pythagorean triplet a = {a}, b = {b}, c = {c} is {a * b * c}.")


# NOTES FOR ME
# The outer loop iterates through possible values of a, starting from 1 and going up to target_sum - 1. This loop iterates through all potential values of a.

# The inner loop iterates through possible values of b, starting from a + 1 and going up to target_sum - a - 1. The reason for starting b from a + 1 is to avoid duplicate combinations of a and b.

# Inside the inner loop, we calculate the value of c using the equation c = target_sum - a - b. This is because we know that a + b + c = target_sum.

# We then check if the current values of a, b, and c form a Pythagorean triplet by using the Pythagorean theorem: a^2 + b^2 = c^2.

# If the Pythagorean condition is satisfied, we found a triplet that meets the criteria. We return the values of a, b, and c.

# If no suitable triplet is found in the loops, the function will return None.


