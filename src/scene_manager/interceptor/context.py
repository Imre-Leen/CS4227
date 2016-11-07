class Context(object):
    def __init__(self, scene_manager):
        self.__scene_manager = scene_manager

    def add_enemy(self, enemy):
        self.__scene_manager.add_object_to_scene(enemy)
