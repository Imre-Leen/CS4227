from interceptor import event_manager
from interceptor.dispatcher import Dispatcher
from random import randint

from src.time_logger import measure_execution_time


class SceneManager:
    def __init__(self, map_generator, default_items=[]):
        self.map_generator = map_generator
        self.map_generator.gen_level()
        self.tilemap = self.map_generator.gen_tiles_level()
        self.default_items = default_items
        self.entities = []
        self.old_entities_x = []
        self.old_entities_y = []
        self.spawn_default_items()
        for entity in self.entities:
            self.update_old_position(entity)
        self.create_dispatchers()

    def update(self):
        for entity in self.entities:
            entity.update(self)
        for entity in self.entities:
            self.check_collision(entity)
            self.update_old_position(entity)

    @measure_execution_time
    def next_level(self, entity):
        self.tilemap = []
        self.map_generator.gen_level()
        self.tilemap = self.map_generator.gen_tiles_level()
        self.entities = []
        self.old_entities_x = []
        self.old_entities_y = []
        self.spawn_default_items()
        return True

    def update_old_position(self, entity):
        if entity in self.entities:
            index = self.entities.index(entity)
            self.old_entities_x[index] = entity.x_pos
            self.old_entities_y[index] = entity.y_pos

    def add(self, entity):
        if entity is not None:
            self.entities.append(entity)
            self.old_entities_x.append(entity.x_pos)
            self.old_entities_y.append(entity.y_pos)

    def remove(self, entity):
        if entity in self.entities:
            index = self.entities.index(entity)
            del self.old_entities_x[index]
            del self.old_entities_y[index]
            self.entities.remove(entity)

    def randomize_position(self, entity):
        entity.x_pos = randint(0, 480)
        entity.y_pos = randint(0, 480)
        while not self.inside_border(entity):
            entity.x_pos = randint(0, 480)
            entity.y_pos = randint(0, 480)

    def check_collision(self, current_entity):
        index = self.entities.index(current_entity)
        for entity in self.entities:
            if current_entity is not entity and self.inside_entity(current_entity, entity):
                if not current_entity.on_entity_collision(entity):
                    self.remove(current_entity)
                continue

        if not self.inside_border(current_entity):
            current_entity.x_pos = self.old_entities_x[index]
            current_entity.y_pos = self.old_entities_y[index]

    def inside_entity(self, entity_a, entity_b):
        if (entity_a.x_pos < entity_b.x_pos + entity_b.width and
            entity_a.x_pos + entity_a.width > entity_b.x_pos and
            entity_a.y_pos < entity_b.y_pos + entity_b.height and
        entity_a.height + entity_a.y_pos > entity_b.y_pos):
            return True
        return False

    def create_dispatchers(self):
        event_manager.scene_manager = self
        dispatcher_1 = Dispatcher(event_types=["keyboard",])
        dispatcher_2 = Dispatcher(event_types=["mouse"])
        event_manager.register(dispatcher_1, "keyboard_events_dispatcher")
        event_manager.register(dispatcher_2, "mouse_events_dispatcher")

    def inside_border(self, current_entity):
        for tile in self.tilemap:
            if not tile.is_walkable and self.inside_entity(current_entity, tile):
                return False
        return True

    def set_default_items(self, items):
        self.default_items = items
        self.spawn_default_items()

    def spawn_default_items(self):
        for item in self.default_items:
            self.randomize_position(item)
            self.add(item)
