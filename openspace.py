
import random
from table import Table
import pandas as pd

class Openspace:
    def __init__(self, number_of_tables, table_capacity):
        """
        Initializes an Openspace object with a specified number of tables and table capacity.
        
        Parameters:
            number_of_tables (int): The number of tables in the Openspace.
            table_capacity (int): The capacity of each table.
        """
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names):
        """
        Organizes the seating arrangement by randomly distributing names among tables.
        
        Parameters:
            names (list): A list of names to be assigned to seats.
        """
        # Shuffle the list of names to distribute randomly
        random.shuffle(names)

        # Calculate the total number of seats in all tables
        total_seats = sum(table.capacity for table in self.tables)

        # If there are more people than available seats, adjust the list of names
        if len(names) > total_seats:
            print("Warning: Not enough seats available for all people.")
            names = names[:total_seats]

        # Iterate over tables and assign seats
        for table in self.tables:
            while table.has_free_spot() and names:
                name = names.pop()
                table.assign_seat(name)

    def display(self):
        """
        Displays the seating arrangement with occupants for each table.
        """
        # Display the tables and their occupants
        print("Open Space Layout:")
        for i, table in enumerate(self.tables, start=1):
            print(f"Table {i}:")
            for j, seat in enumerate(table.seats, start=1):
                if seat.is_occupied():
                    print(f"  Seat {j}: {seat.occupant}")
                else:
                    print(f"  Seat {j}: Empty")

    def store(self, filename):
        """
        Stores the seating arrangement in an Excel file.
        
        Parameters:
            filename (str): The name of the Excel file to store the seating arrangement.
        """
        # Create a dictionary to store table, seat, and occupant data
        data = {'Table': [], 'Seat': [], 'Occupant': []}
        
        # Populate the dictionary with table, seat, and occupant information
        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                data['Table'].append(i)
                data['Seat'].append(j)
                data['Occupant'].append(seat.occupant if seat.is_occupied() else 'Empty')
        
        # Create a DataFrame from the dictionary and store it in an Excel file
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
