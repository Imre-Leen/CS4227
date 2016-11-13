from src.entities.state.state_I import State
from random import randint


class DefaultState(State):
    def __init__(self, entity):
        self.entity = entity

    def change_state(self, context):
        return None

    def do_attack(self, entity):
        return None

    def move(self, context):
        return None

    def do_cleanup(self):
        return None
