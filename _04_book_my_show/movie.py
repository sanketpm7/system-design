class Movie:
    def __init__(self):
        self.id = None
        self.name = None
        self.duration_min = None
    
    def get_id(self) -> int:
        return self.id

    def get_name(self) -> str:
        return self.name

    def get_duration(self) -> str:
        return self.duration_min

    def set_id(self, id) -> None:
        self.id = id

    def set_name(self, name) -> None:
        self.name = name

    def set_durations(self, duration_min) -> None:
        self.duration_min = duration_min