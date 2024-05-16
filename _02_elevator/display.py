from typing import Optional
from enums.directions import Direction

class Display:
    def __init__(self):
        self.floor: int = 0
        self.capacity: int = 0
        self.direction: Optional[Direction] = None
    
    def show_elevator_display(self):
        pass

    def show_hall_display(self):
        pass