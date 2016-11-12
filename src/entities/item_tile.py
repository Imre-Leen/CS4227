from src.graphics.drawable_rectangle import DrawableRectangle
from src.entities.player_tile import PlayerTile


class ItemTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        super(ItemTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)

    def update(self, context):
        return None

    def on_entity_collision(self, entity):
        if type(entity) is PlayerTile:
            return self.pick_up(entity)
        return True

    def pick_up(self, entity):
        return None
