from tile import Tile
from board import Board
from random import randint


class GameController():
    def __init__(self, CELL_SIZE, FIELD_SIZE):
        self.CELL_SIZE = CELL_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.bd = Board(CELL_SIZE, FIELD_SIZE, self)
        self.who_wins = "player"
        self.count_down = -1
        self.game_ended = False
        self.wrote_result = False

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
        COUNT_DOWN_DELAY = 60

        # reset the count down to start the computer move wait time
        if self.bd.lay_down_tile(x, y):
            self.count_down = COUNT_DOWN_DELAY

    def make_computer_move(self):
        """
        Make a computer move
        """
        possible_moves = []
        randomX = randint(0, self.FIELD_SIZE - 1)
        randomY = randint(0, self.FIELD_SIZE - 1)

        # pick a random move until the move is legal and made
        while (not self.has_no_legal_move() and not
               self.bd.lay_down_tile(randomX, randomY)):
            randomX = randint(0, self.FIELD_SIZE - 1)
            randomY = randint(0, self.FIELD_SIZE - 1)

    def input(self, message=''):
        """
        Function to help asking for player name
        """
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def update(self):
        """
        Graphically update tile when playing
        """
        self.bd.draw_board()
        self.bd.update()

        if self.game_ended:
            self.disply_end_text()
            if (not self.wrote_result):
                self.write_score_to_file()
            return

        if (self.has_no_legal_move()):
            self.end_game()
            self.disply_end_text()

        self.count_down -= 1

        # only make computer move after countdown
        if (self.count_down == 0):
            self.make_computer_move()
            self.count_down = -1

    def write_score_to_file(self):
        """
        Helper function to write the game results
        """
        answer = self.input('Enter your name')
        file_name = 'scores.txt'
        scores = [(answer, str(self.bd.player_count))]

        # make sure the file exists
        tmp = open(file_name, 'a')
        tmp.close()

        with open(file_name, 'r') as my_file:
            lines = my_file.read().splitlines()
            for line in lines:
                scores.append(tuple(line.split()))

        scores.sort(key=lambda record: int(record[-1]))
        # make sure list is largest first
        scores.reverse()

        with open(file_name, 'w') as my_file:
            for record in scores:
                for entry in record:
                    my_file.write(entry)
                    my_file.write(" ")
                my_file.write("\n")

        self.wrote_result = True

    def has_no_legal_move(self):
        """
        Check the current board status and determine if there is a legal move
        """
        no_legal_move = True
        for x in range(self.bd.FIELD_SIZE):
            for y in range(self.bd.FIELD_SIZE):
                if ((not (x, y) in self.bd.cells)
                   and self.bd.check_legal(x, y)):
                    no_legal_move = False
        return no_legal_move

    def end_game(self):
        """
        When the board fills up and there are no more legal moves,
        the game is finished
        """
        if (self.game_ended):
            return

        if self.bd.player_count > self.bd.computer_count:
            self.who_wins = "player"
        elif self.bd.player_count < self.bd.computer_count:
            self.who_wins = "computer"
        else:
            self.who_wins = "tie"

        self.game_ended = True

    def disply_end_text(self):
        """
        Give the graphical message about who wins the game (computer/player)
        """
        OFFSET = 3
        FONT_SIZE = 58
        TEXT_COLOR_R = 255
        TEXT_COLOR_G = 192
        TEXT_COLOR_B = 203
        TEXT_SHADE_R = 165
        TEXT_SHADE_G = 186
        TEXT_SHADE_B = 147

        if self.who_wins == "player":
            message = ("Congrats! The " + self.who_wins + " wins. The "
                       + self.who_wins + " has " + str(self.bd.player_count)
                       + " tiles")
        elif self.who_wins == "computer":
            message = ("Congrats! The " + self.who_wins + " wins. The "
                       + self.who_wins + " has " + str(self.bd.computer_count)
                       + " tiles")
        else:
            message = ("Tie! They both have " + str(self.bd.computer_count)
                       + " tiles")

        board_size = self.CELL_SIZE * self.FIELD_SIZE
        center = board_size/2
        rectMode(CENTER)
        textAlign(CENTER, CENTER)
        wordsFont = createFont("BadaboomBB_Reg.otf", FONT_SIZE)
        textFont(wordsFont)
        fill(TEXT_COLOR_R, TEXT_COLOR_G, TEXT_COLOR_B)
        text(message, center+OFFSET, center+OFFSET, board_size, board_size)
        fill(TEXT_SHADE_R, TEXT_SHADE_G, TEXT_COLOR_B)
        text(message, center, center, board_size, board_size)
