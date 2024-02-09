# Openspace Class

The `Openspace` class represents an openspace area with multiple tables for seating.

## Attributes

- `tables` (list): A list of Table objects representing the tables in the openspace.
- `number_of_tables` (int): The total number of tables in the openspace.

## Methods

### `__init__(self, number_of_tables, table_capacity)`

Initializes an Openspace object with a specified number of tables and table capacity.

- Parameters:
  - `number_of_tables` (int): The number of tables in the Openspace.
  - `table_capacity` (int): The capacity of each table. 
    
### `organize(self, names)`

Organizes the seating arrangement by randomly distributing names among tables.

- Parameters:
  - `names` (list): A list of names to be assigned to seats.

### `display(self)`

Displays the seating arrangement with occupants for each table.

### `store(self, filename)`

Stores the seating arrangement in an Excel file.

- Parameters:
  - `filename` (str): The name of the Excel file to store the seating arrangement.


