import threading

class ParkingLot:
  # singleton ParkingLot to ensure only one object of ParkingLot in the system,
  # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
  # similarly exit panels will also use this object to close parking tickets
  instance = None

class __OnlyOne:
  def __init__(self, name, address):
  # 1. initialize variables: read name, address and parking_rate from database
  # 2. initialize parking floors: read the parking floor map from database,
  #    this map should tell how many parking spots are there on each floor. This
  #    should also initialize max spot counts too.
  # 3. initialize parking spot counts by reading all active tickets from database
  # 4. initialize entrance and exit panels: read from database

    self.__name = name
    self.__address = address
    self.__parking_rate = ParkingRate()

    self.__compact_spot_count = 0
    self.__large_spot_count = 0
    self.__motorbike_spot_count = 0
    self.__electric_spot_count = 0

    self.__max_compact_count = 0
    self.__max_large_count = 0
    self.__max_motorbike_count = 0
    self.__max_electric_count = 0

    self.__entrance_panels = {}
    self.__exit_panels = {}
    self.__parking_floors = {}

    # all active parking tickets, identified by their ticket_number
    self.__active_tickets = {}
    self.__lock = threading.Lock()

  def __init__(self, name, address):
    if not ParkingLot.instance:
      ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
    else:
      ParkingLot.instance.__name = name
      ParkingLot.instance.__address = address

  def get_new_parking_ticket(self, vehicle): pass

  def is_full(self, type): pass

  def is_full(self): pass

  def add_parking_floor(self, floor): pass

  def add_entrance_panel(self, entrance_panel): pass

  def add_exit_panel(self,  exit_panel): pass