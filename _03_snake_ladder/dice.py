from random import randint

class Dice:
    def __init__(self, dice_roll_limit):
        self.dice_roll_limit = dice_roll_limit
        self.min = 1
        self.max = 6
    
    def roll_dice(self) -> int:
        total_sum = 0
        for _ in range(self.dice_roll_limit):
            total_sum += randint(self.min, self.max)
        return total_sum