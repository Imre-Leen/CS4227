from src.scene_manager.command.command_I import Command


class MouseLeftClickCommand(Command):
    def __init__(self, player, button):
        self.player = player
        self.button = button
        self.x = 0
        self.y = 0

    def execute(self):
        self.player.x_pos = self.x - 5
        self.player.y_pos = 480 - self.y - 5
