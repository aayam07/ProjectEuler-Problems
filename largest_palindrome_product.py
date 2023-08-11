# Problem - 4: Find the largest palindrome made from the product of two 3-digit numbers


max_palindrome = 0

# to find the largest palindrome it is better to start from the bigger 3 digit numbers i.e 999
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        product = i * j
        str_product = str(product)
        # print(str_product)
        if product > max_palindrome and str_product == str_product[::-1]:
            max_palindrome = product

print(max_palindrome)
