# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
Ans:
product = 1
for i in range(1,11):
    product = product * i
print(f"Product of first 10 natural numbers: {product}")

# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
Ans:
a = 156
b = 7
reaminder = a % b
print(f"Remainder when 156 is divided by 7: {reaminder}")

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
Ans:
a = 25
square = a ** 2
print(f"The Square of {a} is: {square}")

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
Ans:
a = 125
cube_root = a ** (1/3)
print(f"The Cube root of {a} is: {cube_root}")

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
Ans:
a = 12345
sum_of_digits = sum(int(digit) for digit in str(a))
print(f"The sum of digits in {a} is: {sum_of_digits}")


# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
Ans:
a = 97
is_prime = True
for i in range(2, int(a ** 0.5) + 1):
    if a % i == 0:
        is_prime =false
        break
print(f"{a} is a prime number: {is_prime}")

# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
Ans : 
number = 8

factorial = 1

for i in range(1,9):
    factorial *= i
print(f"The factorial of {number} is: {factorial}")


# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
Ans:
numbers = [15,23,31,45,94]
average = sum(numbers)/ len(numbers)
print(f"The average of {numbers} is: {average}")

# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
Ans:
i = 48

h = 36

while h != 0:
    i, h = h, i % h
print(f"The GCD of 48 and 36 is: {i}")


# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
Ans:
sum_odd = sum(range(1, 40, 2))
print(f"The sum of first 20 odd numbers is: {sum_odd}")

