from src.scene_manager.command.command_I import Command


class AttackCommand(Command):
    def __init__(self, entity, button):
        self.entity = entity
        self.button = button

    def execute(self):
        self.entity.attacking = True
