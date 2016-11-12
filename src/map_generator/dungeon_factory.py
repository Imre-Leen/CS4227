from map_factory import MapFactory
from dungeon import Dungeon


class DungeonFactory(MapFactory):
    def __init__(self):
        self.dungeon = Dungeon()

    def get_wall_tile_data(self):
        return self.dungeon.get_wall_tile_data()

    def get_floor_tile_data(self):
        return self.dungeon.get_floor_tile_data()

    def get_inaccessible_tile_data(self):
        return self.dungeon.get_inaccessible_tile_data()