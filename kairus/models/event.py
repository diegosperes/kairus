

class Event:
    @property
    def type(self):
        return self.data.get('type')

    def __init__(self, data):
        self.data = data
