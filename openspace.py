
import random
from table import Table
import pandas as pd

class Openspace:
    def __init__(self, number_of_tables, table_capacity):
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names):
        # Shuffle the list of names
        random.shuffle(names)

        # Iterate over tables and assign seats
        for table in self.tables:
            while table.has_free_spot() and names:
                name = names.pop()
                table.assign_seat(name)

    def display(self):
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
        # Store the seating arrangement in an Excel file
        data = {'Table': [], 'Seat': [], 'Occupant': []}
        for i, table in enumerate(self.tables, start=1):
            for j, seat in enumerate(table.seats, start=1):
                data['Table'].append(i)
                data['Seat'].append(j)
                data['Occupant'].append(seat.occupant if seat.is_occupied() else 'Empty')
        
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
