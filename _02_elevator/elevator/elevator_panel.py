from button.door_button import DoorButton

# instance of ElevatorButton
class ElevatorPanel:
    def __init__(self):
        self.floor_buttons = []
        self.open_btn = DoorButton()
        self.close_btn = DoorButton()