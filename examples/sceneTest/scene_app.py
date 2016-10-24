from commands.move_up_command import MoveUpCommand
from commands.move_left_command import MoveLeftCommand
from commands.move_right_command import MoveRightCommand
from commands.move_down_command import MoveDownCommand
from commands.mouse_left_click import MouseLeftClickCommand
from commands.mouse_right_click import MouseRightClickCommand
from src.entities.map_tile import MapTile
from src.graphics.graphics_app import GraphicsApp
from src.graphics.screen.game_screen import GameScreen
from src.scene_manager.controller.controller import Controller
from src.scene_manager.scene_manager import SceneManager
from src.scene_manager.command.keyCommands import *
from src.scene_manager.controller.input_observer import InputObserver
from random import randint

x = 0
y = 0
map = []
while x < 480:
    while y < 480:
        if randint(1, 100) > 98:
            map.append(MapTile(0.2, 0.0, 0.0, x, y, 20, 20, False))
        else:
            map.append(MapTile(0.0, 0.6, 0.0, x, y, 20, 20, True))
        y += 20
    x += 20
    y = 0

player_controller = Controller()

test_player = MapTile(1.0, 1.0, 0.0, 30, 50, 10, 10, False)
test_player_b = MapTile(1.0, 0.0, 0.5, 380, 350, 10, 10, False)

player_controller.add_command(MoveUpCommand(test_player, "w"))
player_controller.add_command(MoveDownCommand(test_player, "s"))
player_controller.add_command(MoveLeftCommand(test_player, "a"))
player_controller.add_command(MoveRightCommand(test_player, "d"))
player_controller.add_command(MouseRightClickCommand(test_player, RIGHT_CLICK))
player_controller.add_command(MouseLeftClickCommand(test_player, LEFT_CLICK))
scene_manager = SceneManager(map)
graphics_app = GraphicsApp(1, 480, 480, GameScreen(scene_manager), InputObserver())
scene_manager.add_object_to_scene(test_player)
scene_manager.add_object_to_scene(test_player_b)
graphics_app.observer.attach_observer(player_controller)
graphics_app.start()
