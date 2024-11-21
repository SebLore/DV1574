""" ===================================================================
 title:    Laboration 1 part 2
 author:   Sebastian Lorensson
 acronym:  selo16
 date:     20-11-2024
 description:
 Simple program that takes user input and tracks the biggest, smallest, 
 sum of numbers and number of entries, then calculates the adjusted 
 mean.
=================================================================== """

# Intialize variables
nr_of_entries = 0
sum_total = 0

# Take user input (assumed to be a number between -inf and inf)
print("Enter number: ")
number_input = float(input())

# Initialize smallest and biggest with initial user input
biggest = number_input
smallest = number_input

# Run loop until user enters 0. input is assumed to be a valid number
while number_input != 0:
    if number_input > biggest:
        biggest = number_input
    if number_input < smallest:
        smallest = number_input
    sum_total += number_input
    nr_of_entries += 1

    print("Enter number: ")
    number_input = float(input())
# Calculate the adjusted mean by subtracting biggest and smallest
# values.
# nr_of_entries is assumed to be > 3 to prevent 0 divison.
number_mean = (sum_total - biggest - smallest) / (nr_of_entries - 2)

# Print result
print(f"Mean after removing biggest and smallest is: {number_mean:.2f}")
