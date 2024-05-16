from button import Button

class HallButton(Button):
    def __init__(self):
        super.__init__()
        self.pressed_btn_dir = None # UP, DOWN 
    
    def is_pressed(self):
        pass