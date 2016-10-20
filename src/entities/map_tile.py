from OpenGL.GL import *
from src.graphics.drawable_rectangle import DrawableRectangle


class MapTile(DrawableRectangle):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        super(MapTile, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)

