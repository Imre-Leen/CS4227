from src.graphics.drawable_rectangle import DrawableRectangle


class EnemyTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        super(EnemyTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)
        self.attacking = False
        self.phase = 0

    def update(self):
        if self.attacking:
            self.phase += 1
            return self.do_attack(self)
        if self.phase != 0:
            self.phase = 0

    def do_attack(self, entity):
        self.attacking = False

    def on_entity_collision(self, entity):
        return False
