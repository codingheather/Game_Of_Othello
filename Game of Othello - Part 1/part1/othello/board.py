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
        coordinate = [100, 200, 300]
        background(0, 153, 76)
        for i in coordinate:
            strokeWeight(3)
            stroke(0)
            line(i, 0, i, 400)
            line(0, i, 400, i)

    def check_legal(self, position):
        pass

    def lay_down_tile(self, x, y):
        """
        Lay down a black or white tile when necessary
        """
        if (x, y) in self.cells.keys():
            return

        if self.player_turn:
            bl_tile = Tile(x, y, "bl")
            bl_tile.display()
            self.count += 1
            self.player_count += 1
            self.cells[(x, y)] = bl_tile
            self.player_turn = False
        else:
            wh_tile = Tile(x, y, "wh")
            wh_tile.display()
            self.count += 1
            self.computer_count += 1
            self.cells[(x, y)] = wh_tile
            self.player_turn = True
        self.gc.end_game()

    def check_neighbor_tile_color(self, position):
        pass

    def update(self, check_neighbor_tile_color):
        pass
