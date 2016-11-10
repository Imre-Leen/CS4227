class Context(object):
    def __init__(self, scene_manager, event):
        self.__scene_manager = scene_manager
        self.event = event

    def add_enemy(self, enemy):
        self.__scene_manager.add_object_to_scene(enemy)
