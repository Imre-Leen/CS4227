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
from src.scene_manager.interceptor import event_manager
from src.map_generator.map_generator import Generator
from random import randint

from src.entities.player_factory import PlayerFactory
from src.entities.item_factory import ItemFactory
from src.entities.enemy_factory import EnemyFactory

from logging_interceptor import LoggingInterceptor


map_generator = Generator()
map_generator.gen_level()

temp_map = map_generator.gen_tiles_level()
player_controller = Controller()

#test_player = MapTile(1.0, 1.0, 0.0, 30, 50, 5, 5, False)
player_fact = PlayerFactory()
enemy_fact = EnemyFactory()
item_fact = ItemFactory()

player = player_fact.create_player()

normal_enemy = enemy_fact.create_enemy("normal")
boss_enemy = enemy_fact.create_enemy("boss")

health = item_fact.create_item("health")
gold = item_fact.create_item("gold")

#test_player_b = MapTile(1.0, 0.0, 0.5, 380, 350, 10, 10, False)

player_controller.add_command(MoveUpCommand(player, "w"))
player_controller.add_command(MoveDownCommand(player, "s"))
player_controller.add_command(MoveLeftCommand(player, "a"))
player_controller.add_command(MoveRightCommand(player, "d"))
player_controller.add_command(MouseRightClickCommand(player, RIGHT_CLICK))
player_controller.add_command(MouseLeftClickCommand(player, LEFT_CLICK))
scene_manager = SceneManager(temp_map)
graphics_app = GraphicsApp(1, 480, 480, GameScreen(scene_manager), InputObserver())

#Logging
logging_interceptor = LoggingInterceptor()
event_manager.dispatchers["keyboard_events_dispatcher"].register(logging_interceptor)

for name, dispatcher in event_manager.dispatchers.iteritems():
    print name
    print dispatcher.observers_list

scene_manager.add_object_to_scene(player)
scene_manager.add_object_to_scene(normal_enemy)
graphics_app.observer.attach_observer(player_controller)
graphics_app.start()
