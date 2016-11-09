class Dispatcher:
    observers_list = []

    def register(self, observer):
        self.observers_list.append(observer)

    def unregister(self, observer):
        self.observers_list.remove(observer)