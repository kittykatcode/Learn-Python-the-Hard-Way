from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("goldroom",
    """
    this room has gold in it you can grab as much u like,
    there is door to the north. """)
    assert_equal(gold.name, "goldroom")
    assert_equal(gold.path,{})

def test_room_path():
    center = Room("center", "Test room in the center")
    north = Room("North", "test room in the north")
    south = Room("South", "test room in the south")
    center.add_path({'north':north, 'south':south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("start","you can go west and down a hole")
    west = Room("Trees", "There are trees here, you can got to east")
    down = Room("Dungeon", "Its dark down here, you can go up")
    start.add_path({'west':west, 'down':down})
    west.add_path({'east': start})
    down.add_path({'up': start})
    assert_equal(start.go('west'),west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').go('up'),start)
