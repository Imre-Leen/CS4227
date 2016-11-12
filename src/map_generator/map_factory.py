class MapFactory:
    """
    Abstract factory for map tile sets
    """
    def get_wall_tile_data(self):
        raise NotImplementedError

    def get_floor_tile_data(self):
        raise NotImplementedError

    def get_inaccessible_tile_data(self):
        raise NotImplementedError
