from typing import Optional
from jump import Jump

class Cell:
    def __init__(self):
        self.__jump: Optional[Jump] = None 
    
    def set_jump(self, jump: Jump):
        self.__jump = jump 

    def get_jump(self) -> Jump:
        return self.__jump