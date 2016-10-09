from OpenGL.GL import *

class MapTile(object):
    def __init__(self, red_val, green_val, blue_val, x_pos, y_pos, width, height):
        self.red_val = red_val
        self.green_val = green_val
        self.blue_val = blue_val
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

    def draw(self):
        glColor3f(self.red_val, self.green_val, self.blue_val);
        glRectf(-0.5f, 0.5f, 0.5f, -0.5f);