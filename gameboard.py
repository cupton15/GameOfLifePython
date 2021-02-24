from cell import *
from copy import deepcopy

class GameBoard:
    gridsize = 0
    cells = []

    def __init__(self, gridsize):
        self.gridsize = gridsize
        self.populateboard()

    def drawboard(self):
        print("-" * self.gridsize)
        rows = range(self.gridsize)
        for n in rows:
            cols = range(self.gridsize)
            for m in cols:
                cell = next((c for c in self.cells if c.position == Position(n, m, self.gridsize)), None)
                print("o", end="") if cell.alive is True else print("x", end="")
            print("")
        print("-" * self.gridsize)

    def populateboard(self):
        rows = range(self.gridsize)
        for n in rows:
            cols = range(self.gridsize)
            for m in cols:
                self.addcell(n, m)

    def addcell(self, row: int, col: int):
        cell = Cell(Position(row, col, self.gridsize))
        self.cells.append(cell)

    def tick(self):
        self.applyrules()
        self.drawboard()

    def populate_cell(self, position: Position):
        for index, cell in enumerate(self.cells):
            if cell.position == position:
                cell.alive = True
                self.cells[index] = cell
                break

    def applyrules(self):
        shadow_cells = []
        for cell in self.cells:
            try:
                new_cell = deepcopy(cell)
                neighbours = self.get_neighbours(new_cell.position)
                alive_count = sum(1 for n in neighbours if n.alive is True)
                if (alive_count < 2 or alive_count > 3) and new_cell.alive is True:
                    new_cell.alive = False
                elif alive_count == 3 and new_cell.alive is False:
                    new_cell.alive = True
                shadow_cells.append(new_cell)
            except OutOfBoundsError:
                continue
        self.cells = shadow_cells

    def get_neighbours(self, position: Position):
        neighbours = []
        col_range = range(position.col - 1, position.col + 2)
        for col in col_range:
            row_range = range(position.row - 1, position.row + 2)
            for row in row_range:
                try:
                    new_position = Position(col, row, self.gridsize)
                    if new_position == position:
                        continue
                    cell = next((c for c in self.cells if c.position == new_position), None)
                    if cell is not None:
                        neighbours.append(cell)
                except OutOfBoundsError:
                    continue
        return neighbours


