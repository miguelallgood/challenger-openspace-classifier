
class Seat:
    def __init__(self):
        # Initialize a seat as free with no occupant
        self.free = True
        self.occupant = None

    def is_occupied(self):
        # Check if the seat is occupied
        return self.free == False # Checks if self.free is False, indicating that the seat is occupied.

    def set_occupant(self, name):
        # Set an occupant for the seat
        self.free = False
        self.occupant = name

    def remove_occupant(self):
        # Remove occupant from the seat and return the occupant's name
        if not self.free:
            occupant_name = self.occupant
            self.free = True
            self.occupant = None
            return occupant_name
        else:
            return None

class Table:  
    def __init__(self, capacity):
    # Initialize a table with the given capacity and create seats accordingly
        self.capacity = capacity
        self.seats = []
        for seat_index in range(capacity):
            self.seats.append(Seat())

    def has_free_spot(self):
    # Check if the table has any free spot
        for seat in self.seats:
            if not seat.is_occupied():
                return True
                    
    def assign_seat(self, name):
        # Assign a seat to a person
        for seat in self.seats:
            if seat.is_occupied() == False:
                seat.set_occupant(name)
                return True
        return False # If no empty seat is found, we return False.

    def left_capacity(self):
        # Calculate the remaining capacity of the table
        count = 0 # The remaining capacity of the table
        for seat in self.seats: # Iterate over each seat and increment the counter for each seat that is not occupied.
            if not seat.is_occupied():
                count += 1
        return count or 0
