class Check:
    def __init__(self, function):
        self.function=function

    def __call__(self, *args):
        self.function(*args)


