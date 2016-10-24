from src.scene_manager.observer_I import Observer


class InputObserver(Observer):
    def __init__(self):
        self.observer_list = []

    def attach_observer(self, observer):
        if observer not in self.observer_list:
            self.observer_list.append(observer)

    def detach_observer(self, observer):
        try:
            self.observer_list.remove(observer)
        except ValueError:
            pass

    def notify(self, data=None):
        for observer in self.observer_list:
            observer.update(data)