from src.entities.state.state_I import State
from src.entities.player_tile import PlayerTile
from random import randint


class IdleState(State):
    def __init__(self, entity):
        self.entity = entity
        self.x = 0
        self.y = 0

    def change_state(self, context):
        for player in context.entities:
            if type(player) is PlayerTile and self.distance_check(self.entity, player) < 40:
                self.entity.state = self.entity.attack_state

    def do_attack(self, entity):
        return self.entity.attack_state.do_attack(entity)

    def move(self, context):
        if randint(0,6) == 6:
            self.x = randint(-1, 1)
            self.y = randint(-1, 1)

        self.entity.x_pos += self.x
        self.entity.y_pos += self.y

    def do_cleanup(self):
        self.entity.attack_state.do_cleanup()

    def distance_check(self, entity_a, entity_b):
        x_dist = entity_a.x_pos - entity_b.x_pos
        y_dist = entity_a.y_pos - entity_b.y_pos
        return abs(x_dist) + abs(y_dist)