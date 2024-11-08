# dv1574 functions
import math

# exercise 1.8 
def plus(x, y):
    return x+y

# exercise 1.9 
def minus(x, y):
    return x-y

# exercise 1.10
def average(x, y):
    return (x+y)*0.5

# exercise 1.11 
def celsius_to_fahrenheit(c):
    return (c * 1.8) + 32

# exercise 1.12
# height needs to be a decimal of metres. 160 cm is 1.6, for example
def bmi(weight, height):
    return round(weight / (height**2), 1)

# exercise 1.13
def percent(value, total):
    return (value/total) * 100

# exercise 1.14
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
    

# exercise 1.15
def unit(int_num):
    return int_num % 10
def ten(int_num):
    return int_num // 10 % 10
# gets the digit from the nth position from the right
def digit(int_num, pos):
    return int_num // 10**pos % 10

# exercise 1.16
def swap_units_and_tens(int_num):
    u = unit(int_num)
    t = ten(int_num)
    return int_num + u*10 + t - t*10 - u

    

# function tests
print("testing the functions")
print(f"plus:\n  input:1, 2\n  expected output: 3 \n  real output: {plus(1, 2)}")
print(f"minus:\n  input: 2, 1\n  expected output: 1 \n  real output: {minus(2, 1)}")
print(f"average:\n  input: 4, 2\n  expected output: 64.4 \n  real output: {average(4, 2)}")
print(f"celsius_to_fahrenheit:\n  input: 18\n  expected output: 3.0 \n  real output: {celsius_to_fahrenheit(18)}")
print(f"bmi:\n  input: w 80 h 1.8 \n  expected output: 24.7 \n  real output: {bmi(80, 1.8)}")
print(f"percent:\n  input: w 80 h 100 \n  expected output: 80.0 \n  real output: {percent(80, 100)}")
print(f"pythagoras:\n  input: 3, 4 \n  expected output: 5.0 \n  real output: {hypotenuse(3, 4)}")
print(f"unit:\n  input: 123 \n  expected output: 3 \n  real output: {unit(123)}")
print(f"ten:\n  input: 123 \n  expected output: 2 \n  real output: {ten(123)}")
print(f"digit:\n  input: 123456789, 4 \n  expected output: 5 \n  real output: {digit(123456789, 4)}")
print(f"digit:\n  input: 123 \n  expected output: 132 \n  real output: {swap_units_and_tens(123)}")


