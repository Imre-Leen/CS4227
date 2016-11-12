from map_factory import MapFactory
from desert import Desert


class DesertFactory(MapFactory):
    def __init__(self):
        self.desert = Desert()

    def get_wall_tile_data(self):
        return self.desert.get_wall_tile_data()

    def get_floor_tile_data(self):
        return self.desert.get_floor_tile_data()

    def get_inaccessible_tile_data(self):
        return self.desert.get_inaccessible_tile_data()