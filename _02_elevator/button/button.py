from abc import ABC, abstractmethod

class Button(ABC):
    def __init__(self):
        self.status = False
    
    def press_down(self):
        pass

    @abstractmethod
    def is_pressed(self):
        pass