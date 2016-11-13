class State(object):

    def change_state(self, context):
        raise NotImplementedError

    def move(self, context):
        raise NotImplementedError

    def do_attack(self, context):
        raise NotImplementedError

    def do_cleanup(self):
        raise NotImplementedError
