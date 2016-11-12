from map_data import MapData


class Desert(MapData):

    def __init__(self):
        floor_data = (1, 0.8, 0.0)
        wall_data = (0.3, 0.2, 0.01)
        inaccessible_data = (1, 0.8, 0.4)
        super(Desert, self).__init__(floor_data, wall_data, inaccessible_data)
