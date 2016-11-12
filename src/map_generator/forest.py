from map_data import MapData


class Forest(MapData):
    def __init__(self):
        floor_data = (0, 0.5, 0)
        wall_data = (0, 0.2, 0)
        inaccessible_data = (0, 0, 0)
        super(Forest, self).__init__(floor_data, wall_data, inaccessible_data)
