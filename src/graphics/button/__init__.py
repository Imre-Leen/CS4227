"""
Basic extendable button class
"""

from OpenGL.GL import *

class Button(object):
    def __init__(self, text, x_position, y_position, width, height):
        self.text = text
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height

    def draw(self):
        glColor3f(0.5, 0.0, 0.0);
        glRectf(-0.75,0.75, 0.75, -0.75);
