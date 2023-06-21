CELL_SIZE = 100
FIELD_SIZE = 8


def setup():
    global gc
    from board import Board
    from game_controller import GameController
    size(CELL_SIZE * FIELD_SIZE+1,
         CELL_SIZE * FIELD_SIZE+1)

    gc = GameController(CELL_SIZE, FIELD_SIZE)
    gc.start_game()


def draw():
    gc.update()


def mousePressed():
    gc.lay_down_tile(
              (mouseX//CELL_SIZE),
              (mouseY//CELL_SIZE)
              )
