from src.graphics.button import Button


class MainMenu(object):
    def __init__(self):
        # Create Menus with corresponding screens
        self.options = {
            "play game": 1,
            "Load Game": 2,
            "Exit": 3
        }

    def draw(self):
        for menu_option in self.options:
            new_button = Button(menu_option, 0, 0, 100, 100)
            new_button.draw()