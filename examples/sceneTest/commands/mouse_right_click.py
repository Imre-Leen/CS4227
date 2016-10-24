from src.scene_manager.command.command_I import Command


class MouseRightClickCommand(Command):
    def __init__(self, player, button):
        self.player = player
        self.button = button

    def execute(self):
        if self.player.red_val == 1:
            self.player.green_val = 1
            self.player.red_val = 0
        elif self.player.green_val == 1:
            self.player.blue_val = 1
            self.player.green_val = 0
        elif self.player.blue_val == 1:
            self.player.red_val = 1
            self.player.blue_val = 0
        else:
            self.player.red_val = 1
