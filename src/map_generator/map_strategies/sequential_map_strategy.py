from map_strategy import MapStrategy


class SequentialMapStrategy(MapStrategy):
    def __init__(self, map_list):
        self.map_list = map_list
        self.current_map_index = 0

    def choose_map_factory(self):
        if self.current_map_index > len(self.map_list)-1:
            self.current_map_index = 0
        map_factory = self.map_list[self.current_map_index]
        self.current_map_index += 1
        return map_factory

