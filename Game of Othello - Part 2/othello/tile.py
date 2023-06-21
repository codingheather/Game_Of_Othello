class Tile():
    def __init__(self, x, y, color):
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.x = x
        self.y = y
        self.available_colors = [self.BLACK, self.WHITE]
        if color == "bl":
            self.color = self.available_colors[0]
        elif color == "wh":
            self.color = self.available_colors[1]

    def update(self):
        """
        Display a tile
        """
        MULTIPLIER = 100
        OFFSET = 50
        WIDTH = 90
        HEIGHT = 90

        fill(*self.color)
        ellipse(self.x * MULTIPLIER + OFFSET,
                self.y * MULTIPLIER + OFFSET, WIDTH, HEIGHT)

    def flip(self):
        """
        Update the tile to the oppsite color
        """
        if self.color == self.BLACK:
            self.color = self.available_colors[1]
        elif self.color == self.WHITE:
            self.color = self.available_colors[0]
