class Layer():
    def __init__(self, mode, func, coef, **kwargs):
        self.mode = mode
        self.coef = coef
        self.func = func

        self.kwargs = kwargs

        self.data = None

    def call_function(self, result, shape):
        data = self.func(shape, **self.kwargs)
        self.data = data
        if self.mode == 'add':
            data = result + data * self.coef
        elif self.mode == 'mult':
            data = result * data * self.coef
        elif self.mode == 'fit':
            pass
        else:
            print('Layer mode exception')
            data = result
        return data

    def update_settings(self, mode=None, func=None, coef=None, **kwargs):
        if mode:
            self.mode = mode
        if coef:
            self.coef = coef
        if func:
            self.func = func
        for key, value in kwargs.items():
            self.kwargs[key] = value

    def __repr__(self):
        return f'mode = {self.mode}, coef = {self.coef}, func = {self.func}, kwargs = {self.kwargs}'