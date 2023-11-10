# Step 1: Create a variable my_row and set it equal to a list containing the names of 2 people in your row.
my_row = ["Vin slice", "Caleb"]

# Step 2: Using slices, add your name to the end of the list.
my_row += ["Matthew Conelius"]

# Step 3: Create another variable my_row2 and set it equal to my_row.
my_row2 = my_row.copy()

# Step 4: Add a statement that prints my_row2.
print("my_row2:", my_row2)

# Step 5: Add a statement that removes the value at index 1 from my_row.
del my_row[1]

# Step 6: Add a statement that prints my_row.
print("my_row:", my_row)
