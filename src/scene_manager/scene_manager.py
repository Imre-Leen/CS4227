from interceptor import event_manager
from interceptor.dispatcher import Dispatcher


class SceneManager:
    def __init__(self, tilemap=[], entities=[]):
        self.tilemap = tilemap
        self.entities = entities
        self.old_entities_x = [entities.__len__()]
        self.old_entities_y = [entities.__len__()]
        self.update_old_positions()
        self.create_dispatchers()

    def update(self):
        for entity in self.entities:
            self.check_collision(entity)
        self.update_old_positions()

    def update_old_positions(self):
        for entity in self.entities:
            index = self.entities.index(entity)
            self.old_entities_x[index] = entity.x_pos
            self.old_entities_y[index] = entity.y_pos

    def add_object_to_scene(self, object):
        self.entities.append(object)
        self.old_entities_x.append(object.x_pos)
        self.old_entities_y.append(object.y_pos)

    def check_collision(self, current_entity):
        index = self.entities.index(current_entity)
        for entity in self.entities:
            if current_entity is not entity and self.pos_check(current_entity, entity):
                current_entity.x_pos = self.old_entities_x[index]
                current_entity.y_pos = self.old_entities_y[index]
                continue

        for tile in self.tilemap:
            if tile.is_walkable == False and self.pos_check(current_entity, tile):
                current_entity.x_pos = self.old_entities_x[index]
                current_entity.y_pos = self.old_entities_y[index]
                continue

    def pos_check(self, entity_a, entity_b):
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