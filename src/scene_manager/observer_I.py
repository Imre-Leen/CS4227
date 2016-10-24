class Observer(object):
    def attach_observer(self, observer):
        raise NotImplementedError

    def detach_observer(self, observer):
        raise NotImplementedError

    def notify(self, data=None):
        raise NotImplementedError
