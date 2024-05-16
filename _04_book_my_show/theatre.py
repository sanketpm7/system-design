from Enums.city import City
from screen import Screen
from show import Show

class Theatre:
    def __init__(self):
        self.id: int                 = None
        self.address: str            = None
        self.city: City              = None
        self.screens: list[Screen]   = None
        self.shows: list[Show]       = None

    def set_id(self, id) -> None:
        self.id = id

    def set_address(self, address) -> None:
        self.address = address

    def set_city(self, city: City) -> None:
        self.city = city

    def set_screens(self, screens: list[Screen]) -> None:
        self.screens = screens

    def set_shows(self, shows: list[Show]) -> None:
        self.shows = shows

    def get_id(self) -> int: return self.id
    def get_address(self) -> str: return self.address
    def get_city(self) -> City: return self.city
    def get_screens(self) -> list[Screen]: return self.screens 
    def get_shows(self) -> list[Show]: return self.shows