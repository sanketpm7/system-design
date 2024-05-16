class Building:
    building = None

    def __init__(self):
        self.floor    = None   # Floor[]
        self.elevator_list = None   # ElevatorCar[]
    
    @staticmethod
    def get_instance():
        if building == None:
            building = Building()
        return building