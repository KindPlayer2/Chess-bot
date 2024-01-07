"""
This class is responsible for storing information about the current state of a game
It is responsible for valid moves
"""
class GameState():
    def __init__(self):
        #This defines the starting position of a game,8*8 2d array storing all positions
        #-- represents empty space without a piece
        self.board = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]
        self.whiteToMove = True
        self.moveLog = []