from state.default_state import DefaultState
from src.graphics.drawable_rectangle import DrawableRectangle


class EnemyTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        super(EnemyTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)
        self.attacking = False
        self.phase = 0
        self.health = 5
        self.state = DefaultState(self)

    def update(self, context):
        self.state.change_state(context)
        if self.attacking:
            self.phase += 1
            return self.state.do_attack(self)
        if self.phase != 0:
            self.phase = 0
        self.state.move(context)

    def on_entity_collision(self, entity):
        if self.health > 0:
            return True
        else:
            return False
