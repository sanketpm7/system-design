from show import Show
from seat import Seat
from payment import Payment

class Booking:
    def __init__(self):
        self.show: Show = None
        self.booked_seats: list[Seat] = []
        self.payment: Payment = None
    
    def get_show(self):
        return self.show
    
    def get_booked_seats(self):
        return self.booked_seats
    
    def get_payment(self):
        return self.payment
    
    def set_show(self, show):
        self.show = show
    
    def set_booked_seats(self, seats: list[Seat]):
        self.set_booked_seats = seats
    
    def set_payment(self, payment):
        self.payment = payment