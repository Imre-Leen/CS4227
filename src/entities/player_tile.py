from state.default_state import DefaultState
from src.graphics.drawable_rectangle import DrawableRectangle


class PlayerTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        super(PlayerTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)
        self.attacking = False
        self.health = 100
        self.state = DefaultState(self)

    def update(self, context):
        self.state.change_state(context)
        if self.attacking:
            context.add(self.do_attack(self))
        self.state.move(context)

    def on_entity_collision(self, entity):
        if self.health > 0:
            return True
        else:
            self.state.do_cleanup()
            return False

    def do_attack(self, entity):
        self.attacking = False
