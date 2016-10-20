from OpenGL.GL import *
from OpenGL.GLUT import *
from main_menu import MainMenu


from screen_factory import ScreenFactory


class MainMenuFactory(ScreenFactory):
    def __init__(self):
        super(MainMenuFactory, self).__init__()

    def create_screen(self):
        main_menu = MainMenu()
        return main_menu
