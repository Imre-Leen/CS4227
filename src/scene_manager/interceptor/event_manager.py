class EventManager:
    instance = None
    dispatcher_list = []
    observers_list = []

    @staticmethod
    def get_instance(self):
        if self.instance is None:
            self.instance = EventManager()
            return self.instance
        else:
            return self.instance

    def report_event(self, event):
        for observer in self.observers_list:
            observer.notify(event)

    def register(self, observer):
        self.observers_list.append(observer)

    def unregister(self, observer):
        self.observers_list.remove(observer)