class Tile():
    def __init__(self, x, y, color):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        self.x = x
        self.y = y
        self.available_colors = [BLACK, WHITE]
        if color == "bl":
            self.color = self.available_colors[0]
        elif color == "wh":
            self.color = self.available_colors[1]

    def display(self):
        """
        Display a tile
        """
        fill(*self.color)
        ellipse(self.x * 100 + 50, self.y * 100 + 50, 90, 90)

    def update(self, color):
        """
        Update the tile to the oppsite color
        """
        if color == "bl":
            return self.available_colors[1]
        elif color == "wh":
            return self.available_colors[0]
