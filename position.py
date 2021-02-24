from dataclasses import dataclass
from outofboundserror import *

@dataclass(frozen = True)
class Position:
    row: int
    col: int
    max: int

    def __post_init__(self):
        if self.row < 0 or self.row > self.max - 1 or self.col < 0 or self.col > self.max - 1:
            raise OutOfBoundsError

    def __eq__(self, other):
        if not isinstance(other, Position):
            return NotImplemented

        return self.row == other.row and self.col == other.col
