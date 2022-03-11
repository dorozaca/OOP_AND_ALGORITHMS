#decorator en functions

def my_decorator_test(function):
    def wrapper(*args):                      #se necesita un wrapper con *args
        x=int(input('Ingrese 3er term: '))
        y=function(*args)                    #la funcion necesita *args
        return x+y
    return wrapper                           #retorna un wrapper a la misma altura de def


@my_decorator_test
def suma(a,b):
    return a + b


print(suma(10,30))








