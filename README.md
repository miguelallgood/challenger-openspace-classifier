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

## Seat Class

The `Seat` class represents a seat at a table in the open space.

### Attributes:

- `free`: A boolean indicating whether the seat is free or occupied.
- `occupant`: A string representing the name of the occupant of the seat.

### Methods:

- `__init__()`: Initializes a seat as free with no occupant.
- `is_occupied()`: Checks if the seat is occupied.
- `set_occupant(name)`: Sets an occupant for the seat.
- `remove_occupant()`: Removes the occupant from the seat and returns the occupant's name if the seat is occupied.

## Table Class

The `Table` class represents a table in the open space.

### Attributes:

- `capacity`: An integer representing the capacity of the table.
- `seats`: A list of `Seat` objects representing the seats at the table.

### Methods:

- `__init__(capacity)`: Initializes a table with the given capacity and creates seats accordingly.
- `has_free_spot()`: Checks if the table has any free spot.
- `assign_seat(name)`: Assigns a seat to a person.
- `left_capacity()`: Calculates the remaining capacity of the table.

