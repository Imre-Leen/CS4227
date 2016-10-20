"""
Basic extendable button class
"""

from OpenGL.GL import *
from src.graphics.drawable_rectangle import DrawableRectangle


class Button(DrawableRectangle):
    def __init__(self, text, x_pos, y_pos, width, height, red_val, green_val, blue_val):
        self.text = text
        super(Button, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)

    def draw(self, graphics):
        glColor3f(self.red_val, self.green_val, self.blue_val)
        glRectf(self.x_pos, self.y_pos, self.x_pos+self.width, self.y_pos+self.height)
