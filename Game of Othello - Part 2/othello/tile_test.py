from tile import Tile


def test_constructor():
    tl = Tile(3, 4, "bl")
    assert tl.WHITE == (255, 255, 255)
    assert tl.BLACK == (0, 0, 0)
    assert tl.x == 3
    assert tl.y == 4
    assert tl.color == tl.BLACK


def test_flip():
    """Test the flip method"""
    tl = Tile(3, 4, "bl")
    tl.flip()
    assert tl.color == tl.WHITE
