class Player:
    def __init__(self, id, cur_pos):
        self.__id = id
        self.__cur_pos = cur_pos
    
    def set_cur_pos(self, cur_pos) -> None:
        self.__cur_pos = cur_pos

    def get_id(self):
        return self.__id

    def get_cur_pos(self) -> int:
        return self.__cur_pos
