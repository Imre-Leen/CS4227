from src.graphics.drawable_rectangle import DrawableRectangle


class DamageTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height, damage):
        super(DamageTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)
        self.damage = damage

    def update(self, context):
        return None

    def on_entity_collision(self, entity):
        entity.health = entity.health - self.damage
        return True
