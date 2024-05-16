from typing import Optional
from seat import Seat

class Screen:
    def __init__(self):
        self.id = -1
        self.dimension = None
        self.seats: Optional[Seat] = None
    
    def get_id(self): return self.id
    def get_seats(self): return self.seats

    def set_id(self, id):
        self.id = id
    
    def set_seats(self, seats: list[Seat]):
        self.seats = seats