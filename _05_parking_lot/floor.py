from typing import Optional
from display_board import DisplayBoard
from spot import Spot, HandicappedSpot, CompactSpot, LargeSpot, MotorbikeSpot, ElectricSpot 

from Enums.spot_type import SpotType

class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        
        self.__handicapped_spots: Optional[HandicappedSpot] = None
        self.__compact_spots    : Optional[CompactSpot]     = None
        self.__large_spots      : Optional[LargeSpot]       = None
        self.__motorbike_spots  : Optional[MotorbikeSpot]   = None
        self.__electric_spots   : Optional[ElectricSpot]    = None

        self.__info_portals = {}
        self.__display_board = DisplayBoard()

    def get_spot_type(self, spot: Spot):
        pass

    def add_parking_spot(self, spot: Spot):
        pass

    def assign_vehicleToSpot(self, vehicle, spot):
        pass

    def update_display_board_for_handicapped(self, spot):
        pass

    def update_display_board_for_compact(self, spot):
        pass

    def free_spot(self, spot):
        pass