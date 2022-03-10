#decos , inheritance and encapsulation
#dicts

from email.generator import DecodedGenerator


def deco_func(func):
    def wrapper (*args):
        y = 200
        x = func(*args)
        return x + y
    return wrapper


class Deco_class:
    def __init__(self, function):
        self.function=function

    def __call__(self, *args):
        y=100
        x=self.function(*args)
        return y+x


class Animal:
    def __init__(self, family, price, age):
        self.family=family
        self._price=price
        self._age=age

    @property
    def Price(self):
        return self._price

    @Price.setter
    def Price(self,value):
        self._price=value

    @staticmethod
    def voice():
        print('This is a great program')

class Mammal(Animal):
    def __init__(self, price, age, family, habit):  #no necesidad de usar _ pata llamar protected attributes de la clase padre
        super().__init__(price, age, family)
        self.habit=habit


    def muevete(self, habit, alimento='grass'): #cuando se llama esta funcion se necesita pasar un "nuevo habit" que no guardata en el objeto es como si fuera un atributo  nuevo solo para el metodo
        print(f'Tu habito es {habit} y te gusta comer {alimento}')

        self._comiendo(alimento)
        self._durmiendo()

    def _comiendo(self, alimento):
        print(f'esta es tu comida favorita: {alimento}')

    def _durmiendo(self):
        print('Duerme rico!')

    @deco_func
    def numero_de_orejas(self, b, c, a):
        return a*b*c

    @Deco_class
    def numero_de_patas(a, b, c): #cuando se usa class_decorator, dentro de una clase no se necesita self dentro de los parametros
        return a + b + c

    


def run():
    dicty={'Peru':5000, 'Colombia':7000, 'Venezuela':9000, 'Ecuador':4500}
    for i in dicty:
        print(i, dicty[i])

    for keys in dicty.items():   #cuando uso usa .items() para iterar te va a devolver key y value asi no lo pidas como en este caso
        print(keys)

    print(7000 in dicty.values())
    print(('Peru',5000) in dicty.items()) #aca como se usa .items se tiene que usar el item completo entre parentesis para hacer la consulta booleana

    print()

    perro=Mammal(5000,40,'Canine','Licking')
    print(perro.muevete('Besar'))
    print(perro.numero_de_orejas(4,5,6))
    print(perro.numero_de_patas(10,15,5))
    print(perro.Price)
    perro.Price=1000                                 #importante cuando se usa setter no se pasa el valor nuevo entre parentesis se usa igual
    print(perro.Price)
    print(vars(perro))                                
    woff=perro.voice()                               #cuando se usa static method se tiene que asignar a una variable
    print(woff)






if __name__=='__main__':
    run()                                          #cuando se ejecuta el codigo algunos metodos imprimen NONE porque 
    
#son metodos que no retornan valor solo muestran mensaje. Python requiere que todos los metodos retornen valor por eso pinta NONE como una advertencia







