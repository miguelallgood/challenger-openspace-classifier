
import sys

import pandas as pd
from openspace import Openspace

import sys
from openspace import Openspace

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python main.py <excel_filepath> <number_of_tables> <table_capacity>")
        sys.exit(1)

    excel_filepath = sys.argv[1]
    number_of_tables = int(sys.argv[2])
    table_capacity = int(sys.argv[3])

    # Create an instance of Openspace
    openspace = Openspace(number_of_tables, table_capacity)

    # Load the list of people from the Excel file
    try:
        df = pd.read_excel(excel_filepath)
        names = df['Name'].tolist()
    except Exception as e:
        print("Error loading people from Excel file:", e)
        sys.exit(1)

    # Organize the seating arrangement
    openspace.organize(names)

    # Display the assigned people for each table
    openspace.display()


