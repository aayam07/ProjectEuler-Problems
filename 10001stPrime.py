# Problem - 7: Find the 10001st Prime Number

num = 4
count = 2  # considering 2 and 3 as prime numbers and starting to check from 4

while True:
    if count == 10001:
        break  # exit the while loop

    flag = False  # Initialize the flag for each iteration
    for i in range(2, int(num ** 0.5) + 1):  # checking only upto square root of the number
        if num % i == 0:
            flag = True  # true means composite here
            break  # exit the for loop
    
    if not flag:  # If not composite (i.e Prime)
        count += 1
    
    num += 1

print(f"The 10001st Prime Number is: {num - 1}")


        
    
