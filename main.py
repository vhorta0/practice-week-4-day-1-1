# Problem Set: Working with Numbers & Strings in Python

#################### PROBLEM 1: Types of Numbers & Basic Arithmetic ####################
# Task 1: Declare an integer named 'age' with a value of 25.
age = 25
# Print out its type to ensure it's an integer.
print(int(age))
# Task 2: Declare a float named 'height' with a value of 5.9 (which represents someone's height in feet).
height = 5.9
# Print out its type to ensure it's a float.
print(float(height))

# Task 3: What is the data type of the result when 'age' is divided by 'height'?
# Write the code to find out.
print(age / height)

#################### PROBLEM 2: Data Type Conversions ####################
# Task 4: Convert the 'age' to float and 'height' to integer.
# Print out both converted values.
print(float(age))
print(int(height))

# Task 5: Add the original 'age' and 'height' values.
total = age + height
# Convert the result into an integer and then print it.
print(int(total))

#################### PROBLEM 3: Formatting Strings ####################
# Task 6: You are given the following variables:
team_name = "Los Angeles Lakers"
championships_won = 17
# Use string formatting to print: "The Los Angeles Lakers have won 17 championships!"
print(f"The {team_name} have won {championships_won} championships!")

# Task 7: Create two new variables:
points_game1 = 89
points_game2 = 102
# Use string formatting to print: "The team scored 89 points in game 1 and 102 points in game 2."
print(
    f'The team scored {points_game1} in game 1 and {points_game2} in game 2. ')

# Task 8: Calculate the average points across both games and print:
# "The average points over two games is: [average_points]!"
# Ensure average_points is a float with one decimal.
average_points = float((points_game1 + points_game2) / 2)
print(f'The average point over two games is: {average_points}')

# :3

#################### END OF PROBLEM SET ####################
