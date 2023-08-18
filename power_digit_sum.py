# Problem - 16: What is the sum of the digits of the number 2^1000?

number = 2 ** 1000
number_as_str = str(number)
sum = 0

for n in number_as_str:
    digit = int(n)  # convert every character number to integer 
    sum += digit

print(f"The sum of digits of the number 2^1000 = {sum}")