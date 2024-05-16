from Enums.seat_category import SeatCategory 
class Seat:
    def __init__(self):
        self.id = -1
        self.row = -1
        self.category: SeatCategory = None
    
    def get_seat_id(self):
        return self.id 
    
    def set_seat_id(self, id):
        self.id = id
    
    def get_row(self):
        return self.row
    
    def set_row(self, row):
        self.row = row
    
    def get_seat_category(self):
        return self.category
    
    def set_seat_category(self, category: SeatCategory):
        self.category = category