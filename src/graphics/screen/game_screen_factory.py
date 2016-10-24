from OpenGL.GL import *
from OpenGL.GLUT import *
from game_screen import GameScreen


from screen_factory import ScreenFactory


class GameScreenFactory(ScreenFactory):
    def __init__(self):
        super(GameScreenFactory, self).__init__()

    def create_screen(self):
        game_screen = GameScreen()
        return game_screen
