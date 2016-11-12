from src.graphics.button import Button
from screen_I import Screen


class MainMenu(Screen):
    def __init__(self):
        # Create Menus with corresponding screens
        self.options = {
            "play game": 1,
            "Load Game": 2,
            "Exit": 3,
        }

    def draw(self, graphics):
        height = graphics.height
        width = graphics.width
        button_height = height/(len(self.options) + 1)
        button_spacing = button_height/(len(self.options) + 1)
        button_width = width*0.8
        current_height = 0
        for menu_option in self.options:
            current_height += button_spacing
            new_button = Button(menu_option,
                                x_pos=width*0.1,
                                y_pos=current_height,
                                width=button_width,
                                height=button_height,
                                red_val=0.5,
                                green_val=0.0,
                                blue_val=0.0)
            new_button.draw(graphics)
            current_height += button_height

    def update(self):
        pass
