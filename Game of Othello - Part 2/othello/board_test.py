from board import Board
from game_controller import GameController


def test_constructor():
    gc = GameController(100, 8)
    bd = Board(100, 8, gc)
    assert bd.count == 0
    assert bd.player_count == 0
    assert bd.computer_count == 0
    assert bd.cells == {}
    assert bd.opposit_color_position == []
    assert bd.CELL_SIZE == 100
    assert bd.FIELD_SIZE == 8


def test_check_legal():
    """Test the check legal method"""
    gc = GameController(100, 8)
    gc.start_game()
    assert gc.bd.check_legal(3, 2)
    assert not gc.bd.check_legal(5, 2)


def test_check_legal_helper():
    """Test the check legal helper method"""
    gc = GameController(100, 8)
    gc.start_game()
    assert gc.bd.check_legal_helper(3, 2, 0, 1, (255, 255, 255), (0, 0, 0))
    assert not gc.bd.check_legal_helper(
        3, 2, 0, -1, (255, 255, 255), (0, 0, 0))


def test_lay_down_tile():
    """Test the lay down tile method"""
    gc = GameController(100, 8)
    gc.start_game()
    assert gc.bd.lay_down_tile(3, 2)
    assert not gc.bd.lay_down_tile(3, 3)
    assert not gc.bd.lay_down_tile(0, 0)


def test_flip_tile_color():
    """Test the flip tile color method"""
    gc = GameController(100, 8)
    gc.start_game()
    gc.bd.opposit_color_position.append((3, 3))
    gc.bd.flip_tile_color()
    assert gc.bd.cells[(3, 3)].color == gc.bd.cells[(3, 3)].BLACK
