from cell import Cell
from random import randint
from jump import Jump

class Board:
    def __init__(self, size, n_snakes, n_ladders):
        self.size = size 
        self.cells = [ [Cell()] * size for _ in range(size) ]
        self.add_snake(n_snakes)
        self.add_ladder(n_ladders)
    
    def get_cell(self, pos):
        row = pos // self.size
        col = pos % self.size
        return self.cells[row][col]

    '''
    Jump { start, end }:
        snake:  start = head, end = tail   | head > tail 
        ladder: start = bottom, end = top  | bottom < top
    '''
    # Adding snakes
    def add_snake(self, n_snakes) -> None:
        for _ in range(n_snakes):
            head = randint(1, self.size * self.size - 1)
            tail = randint(1, self.size * self.size - 1)

            if tail <= head:
                continue

            jump = Jump(head, tail)
            cell = self.get_cell(head)
            cell.set_jump(jump)
    
    # Adding ladder
    def add_ladder(self, n_ladder) -> None:
        for _ in range(n_ladder):
            bottom = randint(1, self.size * self.size - 1)
            top = randint(1, self.size * self.size - 1)

            if top <= bottom:
                continue

            jump = Jump(bottom, top)
            cell = self.get_cell(bottom)
            cell.set_jump(jump)