from src.scene_manager.observer_I import Observer


class Dispatcher(Observer):

    def __init__(self, event_types=[]):
        self.event_types = event_types
        self.observers_list = []

    def attach_observer(self, observer):
        self.observers_list.append(observer)

    def detach_observer(self, observer):
        self.observers_list.remove(observer)

    def notify(self, data):
        for observer in self.observers_list:
            observer.update(data)

    def event_present(self, event_type):
        return event_type in self.event_types
