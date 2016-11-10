from src.scene_manager.command.command_I import Command


class MoveUpCommand(Command):
    def __init__(self, player, button):
        self.player = player
        self.button = button

    def execute(self):
        self.player.y_pos += 3
