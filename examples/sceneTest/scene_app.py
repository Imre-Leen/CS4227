from commands.move_up_command import MoveUpCommand
from commands.move_left_command import MoveLeftCommand
from commands.move_right_command import MoveRightCommand
from commands.move_down_command import MoveDownCommand
from commands.mouse_left_click import MouseLeftClickCommand
from commands.mouse_right_click import MouseRightClickCommand
from commands.attack_command import AttackCommand
from commands.attacks import Attacks
from third_party_functions.pickup import ThirdPartyPickup
from enemy_states.idle_state import IdleState
from enemy_states.attack_state import AttackState

from src.graphics.graphics_app import GraphicsApp
from src.graphics.screen.game_screen import GameScreen
from src.scene_manager.controller.controller import Controller
from src.scene_manager.scene_manager import SceneManager
from src.scene_manager.command.keyCommands import *
from src.scene_manager.controller.input_observer import InputObserver
from src.scene_manager.interceptor import event_manager
from src.map_generator.map_generator import Generator
from src.map_generator.map_strategies.weighted_map_strategy import WeightedMapStrategy
from src.map_generator.desert_factory import DesertFactory
from src.map_generator.dungeon_factory import DungeonFactory
from src.map_generator.forest_factory import ForestFactory
from random import randint

from src.entities.player_factory import PlayerFactory
from src.entities.item_factory import ItemFactory
from src.entities.enemy_factory import EnemyFactory

from logging_interceptor import LoggingInterceptor

weighted_map_list = [(DungeonFactory(), 50), (DesertFactory(), 25), (ForestFactory(), 25)]
weighted_map_strategy = WeightedMapStrategy(weighted_map_list)
map_generator = Generator(map_strategy=weighted_map_strategy)
player_controller = Controller()
pickup_functions = ThirdPartyPickup()
attack_functions = Attacks()
player_fact = PlayerFactory()
enemy_fact = EnemyFactory()
item_fact = ItemFactory()

player = player_fact.create_player()
player.x_pos = 100
player.y_pos = 150
player.health = randint(3, 100)
player.gold = 0
player.do_attack = attack_functions.short_range_attack

boss_enemy = enemy_fact.create_enemy("boss")

player_controller.add_command(MoveUpCommand(player, "w"))
player_controller.add_command(MoveDownCommand(player, "s"))
player_controller.add_command(MoveLeftCommand(player, "a"))
player_controller.add_command(MoveRightCommand(player, "d"))
player_controller.add_command(MouseRightClickCommand(player, RIGHT_CLICK))
player_controller.add_command(MouseLeftClickCommand(player, LEFT_CLICK))
player_controller.add_command(AttackCommand(player, "i"))

scene_manager = SceneManager(map_generator)
graphics_app = GraphicsApp(1, 480, 480, GameScreen(scene_manager), InputObserver(),
                           title="Example_game_1")

item_list = []
i = 0
while i < 9:
    gold = item_fact.create_item("gold")
    gold.pick_up = pickup_functions.add_gold
    item_list.append(gold)
    i += 1

gold = item_fact.create_item("gold")
gold.pick_up = pickup_functions.add_mega_gold
item_list.append(gold)

health = item_fact.create_item("health")
health.pick_up = pickup_functions.add_health
item_list.append(health)

health = item_fact.create_item("health")
health.pick_up = pickup_functions.minus_health
item_list.append(health)

stairs = item_fact.create_item("stairs")
stairs.pick_up = scene_manager.next_level
item_list.append(stairs)

item_list.append(player)
i=0
while i < 6:
    normal_enemy = enemy_fact.create_enemy("normal")
    normal_enemy.idle_state = IdleState(normal_enemy)
    normal_enemy.attack_state = AttackState(normal_enemy)
    normal_enemy.state = normal_enemy.idle_state
    item_list.append(normal_enemy)
    i += 1

scene_manager.set_default_items(item_list)
graphics_app.observer.attach_observer(player_controller)

#Logging
logging_interceptor = LoggingInterceptor()
event_manager.dispatchers["keyboard_events_dispatcher"].attach_observer(logging_interceptor)

for name, dispatcher in event_manager.dispatchers.iteritems():
    print name
    print dispatcher.observers_list

graphics_app.observer.attach_observer(player_controller)
graphics_app.start()
