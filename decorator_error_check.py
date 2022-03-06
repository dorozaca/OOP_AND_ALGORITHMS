class error_check:
    def __init__(self, function):
        self.function=function

    def __call__(self, *args):  #splat operator
        
        if any(i<0 for i in args):    #importante usar any!
        
            raise ValueError ('No negative')
        else:
            return self.function(*args)


@error_check
def add_positive_number(*args):   #aca va con splat operator
    return sum(args)              #aca sin splat, esto solo para funciones con # de args indefinidos

print(add_positive_number(10,20,-15))