from Enums.spot_type import SpotType

class Spot:
  def __init__(self, number, parking_spot_type):
    self.__number = number
    self.__free = True
    self.__vehicle = None
    self.__parking_spot_type = parking_spot_type

  def get_number(self): return self.__number

  def get_type(self): return self.__parking_spot_type

  def get_vehicle(self): return self.__vehicle

  def is_free(self):
    return self.__free
  
  def assign_vehicle(self, vehicle):
    self.__vehicle = vehicle
    free = False

  def remove_vehicle(self):
    self.__vehicle = None
    free = True

class HandicappedSpot(Spot):
  def __init__(self, number):
    super().__init__(number, SpotType.HANDICAPPED)

class CompactSpot(Spot):
  def __init__(self, number):
    super().__init__(number, SpotType.COMPACT)

class LargeSpot(Spot):
  def __init__(self, number):
    super().__init__(number, SpotType.LARGE)

class MotorbikeSpot(Spot):
  def __init__(self, number):
    super().__init__(number, SpotType.MOTORBIKE)

class ElectricSpot(Spot):
  def __init__(self, number):
    super().__init__(number, SpotType.ELECTRIC)