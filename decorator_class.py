class my_decorator:
    def __init__(self, function):
        self.function=function

    def __call__(self, *args):
        x = int(input('Enter number: '))
        y = self.function(*args)
        print('toto')
        return x+y



@my_decorator
def suma(a,b):
    return a + b

print(suma(60,60))