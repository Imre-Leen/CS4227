from graphics_facade import *

from src.scene_manager.interceptor.event_manager import report_event
from src.scene_manager.interceptor.event import Event

class GraphicsApp(object):
    def __init__(self, window_number, width, height, screen_factory, observer=None, title="Test"):
        self.window_number = window_number  # glut window number
        self.width = width
        self.height = height
        self.screen_factory = screen_factory
        self.title = title
        self.observer = observer

    def start(self):
        # initialization
        create_window(self.width, self.height, self.title)

        glutDisplayFunc(self.runner)  # set runner function callback
        glutIdleFunc(self.runner)  # run method all the time
        glutKeyboardUpFunc(self.key_released)
        glutMouseFunc(self.mouse_click)
        glutSetKeyRepeat(1)
        glutMainLoop()

    def runner(self):
        self.screen_factory.update()
        self.draw()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # clear the screen
        glLoadIdentity()  # reset position
        glOrtho(0, self.width, 0, self.height, -1, 1)
        self.screen_factory.draw(self)

        glutSwapBuffers()  # important for double buffering

    def key_pressed(self, *args):
        information_list = []  # information passed to the observers
        for arg in args:
            information_list.append(arg)
        information_list[0] = "keydown" + str(information_list[0])
        self.observer.notify(args)

    def key_released(self, *args):
        information_list = []  # information passed to the observers
        for arg in args:
            information_list.append(arg)
        information_list[0] = "keyup" + str(information_list[0])
        report_event(Event(information_list, "keyboard"))
        self.observer.notify(args)

    def mouse_click(self, *args):
        information_list = []  # information passed to the observers
        for arg in args:
            information_list.append(arg)
        information_list[0] = "mouse" + str(information_list[0]) + str(information_list[1])
        report_event(Event(information_list, "mouse"))
        self.observer.notify(information_list)



