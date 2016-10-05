from OpenGL.GL import *
from OpenGL.GLUT import *
from screen.main_menu import MainMenu

class GraphicsApp(object):
    def __init__(self, window_number, width, height):
        self.window_number = window_number  # glut window number
        self.width = width
        self.height = height
        self.screen_factory = MainMenu()

    def start(self):
        # initialization
        glutInit()  # initialize glut
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)  # set window size
        glutInitWindowPosition(0, 0)  # set window position
        window = glutCreateWindow("noobtuts.com")  # create window with title
        glutDisplayFunc(self.draw)  # set draw function callback
        glutIdleFunc(self.draw)  # draw all the time
        glutMainLoop()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
        glLoadIdentity()  # reset position

        self.screen_factory.draw()

        glutSwapBuffers()  # important for double buffering

