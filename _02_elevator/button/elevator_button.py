from button import Button

class ElevatorButton(Button):
    def __init__(self):
        super.__init__()
        self.dest_floor_num = -1 
    
    def is_pressed(self):
        pass