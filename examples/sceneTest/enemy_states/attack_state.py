from src.entities.state.state_I import State
from examples.sceneTest.commands.attacks import Attacks
from src.entities.player_tile import PlayerTile


class AttackState(State):
    def __init__(self, entity):
        self.entity = entity
        self.target = None
        self.attack = Attacks()

    def change_state(self, context):
        if not self.target:
            for player in context.entities:
                if type(player) is PlayerTile and self.distance_check(self.entity, player) < 45:
                    self.target = player
            if self.target is None:
                self.entity.state = self.entity.idle_state

        elif not self.distance_check(self.entity, self.target) < 45:
            self.target = None

    def do_attack(self, entity):
        return self.attack.short_range_attack(entity)

    def move(self, context):
            if self.target is not None:
                if self.distance_check(self.entity, self.target) > 10:
                    self.entity.x_pos -= self.direction(self.entity.x_pos - self.target.x_pos)
                    self.entity.y_pos -= self.direction(self.entity.y_pos - self.target.y_pos)
                else:
                    self.entity.attacking = True

    def do_cleanup(self):
        self.attack.damageTile.phase = 0

    def direction(self, number):
        if number > 0:
            return 1
        elif number < 0:
            return -1
        return 0

    def distance_check(self, entity_a, entity_b):
        x_dist = entity_a.x_pos - entity_b.x_pos
        y_dist = entity_a.y_pos - entity_b.y_pos
        return abs(x_dist) + abs(y_dist)