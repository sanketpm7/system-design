class Jump:
    def __init__(self, start, end):
        self.__start: int = start
        self.__end: int = end
    
    def get_start(self) -> int:
        return self.__start
        
    def get_end(self) -> int:
        return self.__end