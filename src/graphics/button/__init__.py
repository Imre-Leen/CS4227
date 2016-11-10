"""
Basic extendable button class
"""

from OpenGL.GL import *
from OpenGL.GLUT import *
from src.graphics.drawable_rectangle import DrawableRectangle


class Button(DrawableRectangle):
    def __init__(self, text, x_pos, y_pos, width, height, red_val, green_val, blue_val):
        self.text = text
        super(Button, self).__init__(x_pos, y_pos, width, height, red_val, green_val, blue_val)

    def draw(self, graphics):
        glColor3f(self.red_val, self.green_val, self.blue_val)
        glRectf(self.x_pos, self.y_pos, self.x_pos+self.width, self.y_pos+self.height)

        # Render the text. Set color to white
        glColor3f(1, 1, 1)#

        # Find the text positioning
        total_chars = self.width/20
        leftover_chars = total_chars - len(self.text)
        extra_x = (leftover_chars/2) * 20
        extra_y = self.height/2
        for ch in self.text :
            glRasterPos(self.x_pos + extra_x, self.y_pos + extra_y)
            glutBitmapCharacter( GLUT_BITMAP_9_BY_15 , ctypes.c_int( ord(ch) ) )
            extra_x += 20