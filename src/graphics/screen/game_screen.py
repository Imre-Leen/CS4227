from screen_I import Screen


class GameScreen(Screen):
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

    def draw(self, graphics):
        for map_tile in self.scene_manager.tilemap:
            map_tile.draw(self)

        for scene_object in self.scene_manager.entities:
            scene_object.draw(self)

    def update(self):
        self.scene_manager.update()
