from graphics_facade import *
from drawable_I import Drawable


class DrawableRectangle(Drawable):
    def __init__(self, x_pos, y_pos, width, height, red_val, green_val, blue_val):
        """
        Instantiates a drawable Rectangle
        :param x_pos: X position in screen coords
        :param y_pos: Y position in screen coords
        :param width: Width in screen coords
        :param height: Height in screen coords
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.red_val = red_val
        self.green_val = green_val
        self.blue_val = blue_val

    def draw(self, graphics):
        draw_rectangle(self.x_pos, self.y_pos, self.width, self.height, self.red_val,
                       self.green_val, self.blue_val)