
import sys
from utils.openspace import Openspace

# Prompt the user to enter the Excel file path
colleagues_filepath = input("Enter the Excel file path: ")

# Define the number of tables and the capacity of each table
number_of_tables = 6
table_capacity = 4
    
# Create an instance of the Openspace class with the specified number of tables and table capacity
openspace = Openspace(number_of_tables, table_capacity)

# Load the list of people from the CSV file
try:
    with open(colleagues_filepath, 'rb') as file:
        # Read the CSV file 
        data = []
        for line in file:            
            row = line.decode('UTF-8').split()
            data.append(row)
    names = [row[0] for row in data[1:]]  # Extract the list of names from the data
except Exception as e:
    # Handle the error if there's an issue loading people from the CSV file
    print("Error loading people from Excel file:", e)
    sys.exit(1)

# Organize the seating arrangement by distributing the names randomly among the tables
openspace.organize(names)

# Display the assigned people for each table
openspace.display()

# Stores the seating arrangement in a CSV file
openspace.store(colleagues_filepath)

# Calculate and display how many seats are left after the seating arrangement
total_seats = number_of_tables * table_capacity  # Calculate the total number of seats in all tables

occupied_seats = 0  # Initialize the total number of occupied seats
for table in openspace.tables: # Iterate over each table in the Openspace
    # Calculate the number of occupied seats for the current table
    occupied_seats += len(table.seats) - table.left_capacity() # The variable occupied_seats now holds the total number of occupied seats

remaining_seats = total_seats - occupied_seats  # Calculate the remaining number of seats
print(f"Total seats: {total_seats}")  # Display the total number of seats
print(f"Occupied seats: {occupied_seats}")  # Display the total number of occupied seats
print(f"Remaining seats: {remaining_seats}")  # Display the remaining number of seats


