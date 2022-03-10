from mimetypes import init
from multiprocessing.sharedctypes import Value


class Artefacto:
    def __init__(self, marca, year):
        self.marca=marca
        self._year=year

    @property                   #getter van identados a la misma altura de cualquier metodo
    def Year(self):
        return self._year

    @Year.setter                 #setter van identados a la misma altura de cualquier metodo
    def Year(self,value):
        self._year=value

    @staticmethod
    def garantia():
        print(f'Tiene 9 meses de garantia a todo costo')    

        

class Lavadora(Artefacto):
    def __init__(self, marca, year, color):
        super().__init__(marca, year)
        self.color=color

    def lavar(self, temperatura='hot'):   #Esta es una interface
        self._llenar_tanque(temperatura)
        self._anadir_jabon()
        self._lavar() #This method is protected and it is different from main method
        self._centrifugar()

    def _llenar_tanque(self, temperatura):
        print(f'Llenando tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print(f'agregando jabon')

    def _lavar(self):
        print(f'Lavando papa')

    def _centrifugar(self):
        print('Centrifugando')

if __name__== '__main__':
    milavadora=Lavadora('Oster',1990,'rojo')
    print(milavadora.marca)
    print(milavadora.Year)
    milavadora.lavar()
    
    #print(id(milavadora))
    #print(hex(id(milavadora)))

    