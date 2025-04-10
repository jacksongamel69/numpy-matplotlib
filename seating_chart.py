import numpy as np
from numpy import random

# Author - Jackson Gamel
# Sci Computing SP 25


rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of chairs per row: "))
total_seats = rows * cols

# Student name list
names = [
    "Alice", "Bob", "Charlie", "David", "Ella", "Brenna", "Grace", "Henry",
    "Shaan", "Jackson", "Bert", "Mark", "Gavin", "Nate", "Olivia", "Pete",
    "April", "Rachel", "Sam", "Tina", "Advait", "Victor", "Wendy", "Xander",
    "Yasmine", "Zach", "Aaron", "Bella", "Cody", "Diana", "Eli", "Albert"
]

if len(names) < total_seats:
    print("Not enough student names! Please add more to the list.")
    exit()

# Randomize and reshape names into a 2D array
selected_names = random.choice(names, total_seats, replace=False)
seating_chart = np.array(selected_names).reshape(rows, cols)

# Print seating chart with names and coordinates
print("\nSeating Chart:")
for i in range(rows):
    row_output = ""
    for j in range(cols):
        name = seating_chart[i][j]
        row_output += f"{name} ({i+1},{j+1})".ljust(20)  # Include coordinates and align the output
    print(row_output)
