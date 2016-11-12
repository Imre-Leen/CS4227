import random
from desert_factory import DesertFactory
from dungeon_factory import DungeonFactory
from forest_factory import ForestFactory

if __name__ == "__main__":
    random = random.randint(0, 2)
    if random == 1:
        print "haha"
        map_factory = DesertFactory()
    elif random == 2:
        print "hehe"
        map_factory = DungeonFactory()
    else:
        print "huhu"
        map_factory = ForestFactory()

    print map_factory
    print map_factory.get_floor_tile_data()
    print map_factory.get_inaccessible_tile_data()
    print map_factory.get_wall_tile_data()