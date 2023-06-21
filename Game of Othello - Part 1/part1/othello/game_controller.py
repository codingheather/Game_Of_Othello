from tile import Tile
from board import Board


class GameController():
    def __init__(self, CELL_SIZE, FIELD_SIZE, wordsFont):
        self.CELL_SIZE = CELL_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.bd = Board(CELL_SIZE, FIELD_SIZE, self)
        self.wordsFont = wordsFont
        self.who_wins = "player"
        self.bd.draw_board()

    def start_game(self):
        """
        the game begins with 4 tiles in the middle
        two white and two black
        """
        self.bd.lay_down_tile(self.FIELD_SIZE//2, self.FIELD_SIZE//2-1)
        self.bd.lay_down_tile(self.FIELD_SIZE//2-1, self.FIELD_SIZE//2-1)
        self.bd.lay_down_tile(self.FIELD_SIZE//2-1, self.FIELD_SIZE//2)
        self.bd.lay_down_tile(self.FIELD_SIZE//2, self.FIELD_SIZE//2)

    def lay_down_tile(self, x, y):
        """
        Lay down a tile
        """
        self.bd.lay_down_tile(x, y)

    def update(self):
        pass

    def end_game(self):
        """
        When the board fills up and there are no more legal moves,
        the game is finished
        """
        if self.bd.count == (self.FIELD_SIZE ** 2):
            if self.bd.computer_count < self.bd.player_count:
                self.who_wins = "player"
                self.disply_end_text(self.bd.player_count, self.who_wins)
            elif self.bd.computer_count > self.bd.player_count:
                self.who_wins = "computer"
                self.disply_end_text(self.bd.computer_count, self.who_wins)
            else:
                self.who_wins = "tie"
                self.disply_end_text(self.bd.computer_count, self.who_wins)

    def disply_end_text(self, count, who_wins):
        """
        Give the message about who wins the game (computer/player)
        """
        if who_wins == "player" or who_wins == "computer":
            message = ("Congrats! The " + who_wins + " wins. The "
                       + who_wins + " has " + str(count) + " tiles")
        else:
            message = "Tie! They both have " + str(count) + " tiles"
        board_size = self.CELL_SIZE * self.FIELD_SIZE
        center = board_size/2
        offset = 3
        rectMode(CENTER)
        textAlign(CENTER)
        textFont(self.wordsFont)
        fill(255, 192, 203)
        text(message, center+offset, center+offset, board_size, board_size)
        fill(165, 186, 147)
        text(message, center, center, board_size, board_size)
