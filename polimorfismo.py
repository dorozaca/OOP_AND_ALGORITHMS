class Persona:
    def __init__(self, name):
        self.name=name

    def transportandome(self):
        print('Me voy a pie')

class Ciclista(Persona):
    def __init__(self, name):
        super().__init__(name)

    def transportandome(self):
        super().transportandome(self)
        print('Me voy en bicicleta')

class Automovilista(Persona):
    def __init__(self,name):
        super().__init__(name)

    def transportandome(self):
        print('Me voy en auto')

class Burrero(Persona):
    def __init__(self,name):
        super().__init__(name)

    def transportandome(self):
        print('Me voy en burro')

def transportando_personas(objeto):  #this independent fuction is key to understand polymorphism, because it takes object as argument and calls ohject's method.
    objeto.transportandome()

def run():                                
    juansito=Burrero('champ')
    transportando_personas(juansito) #By using the aforementioned function we'll get the correspoding method executed and we could even encapsulate "transportandome" methods within each class 
    #juansito.transportandome() # esto hace lo mismo pero es menos elegante

if __name__=='__main__':
    run()
