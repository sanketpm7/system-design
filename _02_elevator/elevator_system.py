class ElevatorSystem:
    system_instance = None 

    def monitering(self):
        pass

    def dispatcher(self):
        pass

    # seperate constructor - prevent direct instantation
    def ElevatorSystem(self):
        self.building = None    # Building
    
    # singleton pattern: Single instance of the system
    @staticmethod
    def get_instance(self):
        if system_instance == None:
            system_instance = ElevatorSystem()
        return system_instance