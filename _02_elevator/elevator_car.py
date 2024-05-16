from typing import Optional

class ElevatorCar:
    def __init__(self):
        self.id = 0         # int
        self.door = None    # Door
        self.state = None   # ElevatorState
        self.display = None # Display
        self.panel = None   # ElevatorPanel
    
    def move() -> None: pass
    def stop() -> None: pass

    def open_door() -> None: pass
    def close_door() -> None: pass