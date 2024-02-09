
import sys
import pandas as pd
from openspace import Openspace

# Prompt the user to enter the Excel file path
excel_filepath = input("Enter the Excel file path: ")

# Define the number of tables and the capacity of each table
number_of_tables = 6
table_capacity = 4
    
# Create an instance of the Openspace class with the specified number of tables and table capacity
openspace = Openspace(number_of_tables, table_capacity)

# Load the list of people from the Excel file
try:
    df = pd.read_excel(excel_filepath) # Read data from the Excel file
    names = df['Name'].tolist() # Extract the list of names from the DataFrame
except Exception as e:
    # Handle the error if there's an issue loading people from the Excel file
    print("Error loading people from Excel file:", e)
    sys.exit(1)

# Organize the seating arrangement by distributing the names randomly among the tables
openspace.organize(names)

# Display the assigned people for each table
openspace.display()

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


