from map_data import MapData


class Dungeon(MapData):
    def __init__(self):
        floor_data = (0.8, 0.8, 0.8)
        wall_data = (0.3, 0.3, 0.3)
        inaccessible_data = (0.2, 0.2, 0.2)
        super(Dungeon, self).__init__(floor_data, wall_data, inaccessible_data)