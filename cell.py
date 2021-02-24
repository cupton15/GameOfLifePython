from position import *

class Cell:
    alive = False
    position: Position

    def __init__(self, position: Position, alive=False):
        self.position = position
        self.alive = alive

