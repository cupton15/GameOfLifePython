from gameboard import *

def startgame():
    board = GameBoard(10)
    board.populate_cell(Position(2, 2, 10))
    board.populate_cell(Position(3, 2, 10))
    board.populate_cell(Position(2, 3, 10))
    board.populate_cell(Position(3, 3, 10))
    board.populate_cell(Position(4, 4, 10))
    board.populate_cell(Position(5, 4, 10))
    board.populate_cell(Position(4, 5, 10))
    board.populate_cell(Position(5, 5, 10))
    board.drawboard()

    user_input = ""
    while user_input != "q":
        board.tick()
        user_input = input()

if __name__ == '__main__':
    startgame()
