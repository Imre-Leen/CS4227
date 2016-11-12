from src.graphics.drawable_rectangle import DrawableRectangle


class MapTile(DrawableRectangle):
    def __init__(self, red_val=0, green_val=0, blue_val=0, x_pos=0, y_pos=0, width=1, height=1,
                 is_walkable=True):
        super(MapTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)
        self.is_walkable = is_walkable

