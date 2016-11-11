from src.scene_manager.command.command_I import Command


class MoveLeftCommand(Command):
    def __init__(self, player, button):
        self.player = player
        self.button = button

    def execute(self):
        self.player.x_pos -= 3
