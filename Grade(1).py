"""
This program asks the user for the score and displays the letter grade.
The score will be rounded to the nearest integer before calculating the
letter grade.

by Mahadev
"""

# ask user for a number, round it and store in variable score
score = round(float(input("Please enter your score: ")))

# compute letter grade based on the range and store in grade
if (score < 0):
    grade = "invalid"
elif (score < 60):
    grade = "F"
elif (score < 70):
    grade = "D"
elif (score < 80):
    grade = "C"
elif (score < 90):
    grade = "B"
elif (score <= 100):
    grade = "A"
else:
    grade = "invalid"

# display the grade
print("Your grade is ", end="")
print(grade)
