class MapData(object):

    def __init__(self, floor_data, wall_data, inaccessible_data):
        self.__floor_data = floor_data
        self.__wall_data = wall_data
        self.__inaccessible_data = inaccessible_data

    def get_floor_tile_data(self):
        """
        Get floor tile data
        :return: tuple following format (red_val, green_val, blue_val)
        """
        return self.__floor_data

    def get_wall_tile_data(self):
        """
        Get wall tile data
        :return: tuple following format (red_val, green_val, blue_val)
        """
        return self.__wall_data

    def get_inaccessible_tile_data(self):
        """
        Get inaccessible tile data
        :return: tuple following format (red_val, green_val, blue_val)
        """
        return self.__inaccessible_data
