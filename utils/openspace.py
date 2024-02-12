
import random
from .table import Table

class Openspace:
    """
    Represents an openspace area with multiple tables for seating.
    
    Attributes:
        tables (list): A list of Table objects representing the tables in the openspace.
        number_of_tables (int): The total number of tables in the openspace.
    """

    def __init__(self, number_of_tables, table_capacity):
        """
        Initializes an Openspace object with a specified number of tables and table capacity.
        
        Parameters:
            number_of_tables (int): The number of tables in the Openspace.
            table_capacity (int): The capacity of each table.
        """
        self.tables = []  # Initialize an empty list to store the tables

        # Create each table and add it to the list
        for _ in range(number_of_tables):
            table = Table(table_capacity)  # Create a new table with the specified capacity
            self.tables.append(table)  # Add the table to the list of tables       

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
        Stores the seating arrangement in a CSV file.

        Parameters:
            filename (str): The name of the CSV file to store the seating arrangement.
        """        
        # Write the data to a CSV file
        with open(filename, 'w') as csvfile:
            # Write the header row
            csvfile.write("Table,Seat,Occupant\n")           
            
            # Initialize counters for table and seat numbers
            table_number = 1
                # Write the data rows
            for table in self.tables:
                seat_number = 1
                for seat in table.seats:
                    occupant = seat.occupant if seat.is_occupied() else 'Empty'
                    csvfile.write(f"{table_number},{seat_number},{occupant}\n")
                    seat_number += 1
                table_number += 1
            
