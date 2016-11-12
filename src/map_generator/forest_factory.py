from map_factory import MapFactory
from forest import Forest


class ForestFactory(MapFactory):
    def __init__(self):
        self.forest = Forest()

    def get_wall_tile_data(self):
        return self.forest.get_wall_tile_data()

    def get_floor_tile_data(self):
        return self.forest.get_floor_tile_data()

    def get_inaccessible_tile_data(self):
        return self.forest.get_inaccessible_tile_data()