from map_strategy import MapStrategy
import random


class WeightedMapStrategy(MapStrategy):
    def __init__(self, weighted_map_list):
        """
        Constructor
        :param weighted_map_list: List of tuples in format
        [(map_factory_instance, weigth),...]
        """
        self.weighted_map_list = weighted_map_list

    def choose_map_factory(self):
        total_weight = sum([element[1] for element in self.weighted_map_list])
        random_num = random.randint(0, total_weight-1)
        current_num = 0
        for element in self.weighted_map_list:
            current_num += element[1]
            if current_num >= random_num:
                return element[0]

