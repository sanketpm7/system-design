from abc import ABC, abstractmethod
from Enums.account_status import AccountStatus

class Account(ABC):
    def __init__(self, user_name, password, person, status = AccountStatus.ACTIVE):
        self.usernmae = user_name
        self.password = password
        self.person   = person
        self.status   = status

    @abstractmethod
    def reset_passwd(self):
        None

class Admin(Account):
    def __init__(self, user_name, password, person, status=AccountStatus.Active):
        super().__init__(user_name, password, person, status)

    def add_floor(self, floor): None
    def add_spot(self, floor_name, spot): None

    def add_display_board(self, floor_name, display_board): None
    def add_customer_info_panel(self, floor_name, info_panel): None

    def add_entrance_panel(self, entrance_panel): None
    def add_exit_panel(self, exit_panel): None

class ParkingAttendant(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def process_ticket(self, ticket_number):
    None