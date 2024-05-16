from movie import Movie
from screen import Screen

class Show:
    def __init__(self):
        self.id: int = None
        self.movie: Movie = None
        self.screen: Screen = None
        self.start_time: int = None
        self.booked_seat_ids: list[int] = None
    
    '''
    setters
    getters
    '''
    
    def set_show_id(self, id) -> None:
        self.id = id

    def set_movie(self, movie) -> None:
        self.movie = movie

    def set_screen(self, screen) -> None:
        self.screen = screen

    def set_start_time(self, start_time) -> None:
        self.start_time = start_time

    def set_booked_seat_ids(self, booked_seat_ids: list[int]) -> None:
        self.booked_seat_ids = booked_seat_ids

    def get_show_id(self) -> int:
        return self.id
    
    def get_movie(self) -> Movie:
        return self.movie
    
    def get_screen(self) -> Screen:
        return self.screen
    
    def get_start_time(self) -> int:
        return self.start_time
    
    def get_booked_seat_ids(self) -> list[int]:
        return self.booked_seat_ids