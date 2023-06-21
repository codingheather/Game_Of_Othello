from tile import Tile


class Board():
    def __init__(self, CELL_SIZE, FIELD_SIZE, gc):
        self.CELL_SIZE = CELL_SIZE
        self.FIELD_SIZE = FIELD_SIZE
        self.count = 0
        self.player_turn = True
        self.player_count = 0
        self.computer_count = 0
        self.cells = {}
        self.gc = gc
        self.check_position = [-1, 0, 1]
        self.opposit_color_position = []

    def draw_board(self):
        """
        Draw the board
        """
        COORDINATES = [100, 200, 300, 400, 500, 600, 700]
        BACKGROUND_R = 0
        BACKGROUND_G = 153
        BACKGROUND_B = 76
        STROKE_WEIGHT = 3
        COORDINATE = 800

        background(BACKGROUND_R, BACKGROUND_G, BACKGROUND_B)

        for i in COORDINATES:
            strokeWeight(STROKE_WEIGHT)
            stroke(0)
            line(i, 0, i, COORDINATE)
            line(0, i, COORDINATE, i)

    def check_legal(self, x, y):
        """
        Check whether the tile that laid down by the player
        is in a legal position
        """
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        self.opposit_color_position = []
        legal = False

        for i in self.check_position:
            for j in self.check_position:
                # no need to check clicked position
                if not (i == 0 and j == 0):
                    if self.player_turn:
                        if self.check_legal_helper(x, y, i, j,
                                                   WHITE, BLACK):
                            legal = True
                    else:
                        if self.check_legal_helper(x, y, i, j,
                                                   BLACK, WHITE):
                            legal = True
        # checked all eight neighbors didn't find any tile
        return legal

    def check_legal_helper(self, x, y, i, j, opposite_color, current_color):
        """
        Helper function to check if a move is legal
        """
        opposite_count = 0
        temp_opposite_list = []
        # skip all opposite tiles and add to flip list
        current_coordinates = (x + i, y + j)
        while (current_coordinates in self.cells and
                self.cells[current_coordinates].color == opposite_color):
            opposite_count += 1
            temp_opposite_list.append(current_coordinates)
            current_coordinates = (current_coordinates[0] + i,
                                   current_coordinates[1] + j)

        # there is a current tiles and there is a computer tile
        # to flip in between
        if (current_coordinates in self.cells and
           opposite_count > 0 and
           self.cells[current_coordinates].color == current_color):
            self.opposit_color_position += temp_opposite_list
            return True

        return False

    def lay_down_tile(self, x, y):
        """
        Lay down a black or white tile when necessary
        """
        if (x, y) in self.cells.keys():
            return False

        if self.count >= 4 and not self.check_legal(x, y):
            return False

        if self.player_turn:
            bl_tile = Tile(x, y, "bl")
            # bl_tile.display()
            self.count += 1
            self.player_count += 1
            self.cells[(x, y)] = bl_tile
            self.player_turn = False
        else:
            wh_tile = Tile(x, y, "wh")
            # wh_tile.display()
            self.count += 1
            self.computer_count += 1
            self.cells[(x, y)] = wh_tile
            self.player_turn = True

        self.flip_tile_color()
        return True

    def flip_tile_color(self):
        """
        Flip tile color as needed
        """
        for coordinate in self.opposit_color_position:
            tile = self.cells[coordinate]
            if (tile.color == tile.BLACK):
                self.player_count -= 1
                self.computer_count += 1
            else:
                self.player_count += 1
                self.computer_count -= 1
            self.cells[coordinate].flip()

    def update(self):
        """
        Update and display updated tile
        """
        for tile in self.cells:
            self.cells[tile].update()
