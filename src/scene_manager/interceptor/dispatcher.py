class Dispatcher:

    def __init__(self, event_types=[]):
        self.event_types = event_types
        self.observers_list = []

    def register(self, observer):
        self.observers_list.append(observer)

    def unregister(self, observer):
        self.observers_list.remove(observer)

    def notify(self, context):
        for observer in self.observers_list:
            observer.update(context)

    def event_present(self, event_type):
        return event_type in self.event_types
