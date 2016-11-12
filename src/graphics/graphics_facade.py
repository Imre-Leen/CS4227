"""
Facade for openGL and GLUT methods.
"""

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_rectangle(x_pos, y_pos, width, height, red_val, green_val, blue_val):
    glColor3f(red_val, green_val, blue_val)
    glRectf(x_pos, y_pos, x_pos + width, y_pos + height)


def create_window(width, height, title):
    glutInit()  # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)  # set window size
    glutInitWindowPosition(0, 0)  # set window position
    glutCreateWindow(title)  # create window with title'


def set_color(red, green, blue):
    glColor3f(red, green, blue)

def draw_character(x, y, character):
    glRasterPos(x, y)
    glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(character)))