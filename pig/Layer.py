class Layer:
    def __init__(self, func, **kwargs):
        self.func = func

        self._kwargs = kwargs

        self._data = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    def set_empty_data(self, length, width):
        self._data = [[0 for _ in range(length)] for _ in range(width)]

    def call_function(self):
        self._data = self.func(self._data, **self._kwargs)

    def update_settings(self, func=None, **kwargs):
        if func:
            self.func = func
        for key, value in kwargs.items():
            self._kwargs[key] = value

    def __repr__(self):
        return f'mode = func = {self.func}, kwargs = {self._kwargs}'