from game_controller import GameController


def test_constructor():
    gc = GameController(100, 8)
    assert gc.CELL_SIZE == 100
    assert gc.FIELD_SIZE == 8
    assert gc.who_wins == "player"
    assert gc.count_down == -1
    assert not gc.game_ended
    assert not gc.wrote_result


def test_start_game():
    """Test the start game method"""
    gc = GameController(100, 8)
    gc.start_game()
    assert len(gc.bd.cells) == 4


def test_lay_down_tile():
    gc = GameController(100, 8)
    gc.start_game()
    gc.lay_down_tile(3, 2)
    assert gc.count_down == 60


def test_make_computer_move():
    gc = GameController(100, 8)
    gc.start_game()
    gc.lay_down_tile(3, 2)
    gc.make_computer_move()
    assert len(gc.bd.cells) == 6


def test_has_no_legal_move():
    gc = GameController(100, 8)
    assert gc.has_no_legal_move()
    gc.start_game()
    assert not gc.has_no_legal_move()


def test_end_game():
    gc = GameController(100, 8)
    assert not gc.game_ended
    gc.end_game()
    assert gc.game_ended
