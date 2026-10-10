# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
# Ans:
numbers = [3.14, 2.718, 1.618, 0.577]
Average = sum(numbers)/len(numbers)
print(f"The average of {numbers} is: {Average}")

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
# Ans: Used Chatgpt
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")

# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
# Ans: Used ChatGPT
principal = 1000
rate = 5.5 / 100
time = 3
compound_interest = principal * (1 + rate) ** time - principal
print(f"The compound interest on ${principal} at {rate*100}% for {time} years is: ${compound_interest:.2f}")

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
# Ans:
a = 3.5
b = 4.2
c = sqrt(a**2 + b**2)
print("The hypotenuse is:", c)

# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
# Ans:
radius = 7.8
volume = 4/3 * 3.14159 * (radius ** 3)
print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")


# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
# Ans: method - 1
Pi_value = 3.14159
print(f"Rounded value using f-string: {Pi_value:.3f}")
# Ans: method - 2
rounded_value = round(3.14159, 3)
print("Rounded value:", rounded_value)

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
# Ans:
percentage = (45 / 67) * 100
print(f"The percentage of 45 out of 67 is: {percentage:.2f}%")

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
# Ans:
Square_root = 23.456 ** 0.5
print(f"The square root of 23.456 is: {Square_root:.3f}")

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
# Ans: 
prinicial = 2500
rate = 6.5
time = 2.5
simple_interest = (prinicial * rate * time) / 100
print("The simple interest is:", simple_interest)

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
# Ans:
degrees = 45.7 
pi_value = 3.14159
radians = degrees * (pi_value / 180)
print("The angle in radians is:", radians)
