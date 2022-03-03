class Coordenada:
    def __init__(self, x, y, number) : #"Some people teach that _x is Python's equivalent of protected, and __x its equivalent of private, but that's very misleading."
        self.x=x
        self.y=y
        self._number=number

        @property
        def Number(self):
            return self._number

        @Number.setter #it seems like we can use lower case here
        def Number(self,value):
            self._number=value

    @staticmethod
    def my_method():
        print('La hiciste')


    def distancia(self, second_coordenada):
        x_diff=(self.x-second_coordenada.x)**2
        y_diff=(self.y-second_coordenada.y)**2

        return (x_diff-y_diff)**0.5

if __name__== '__main__':
    coord1=Coordenada(10,50,7)
    coord2=Coordenada(5,40,20)

    print(vars(coord1))
    print(coord1.distancia(coord2))     #callling another instance within a methon
    coord1.Number=30
    coord1.Number=100
    container=coord1.Number
    
    print(f'My nombre es {coord1.Number}')
    print(vars(coord1))
    print(isinstance(coord1, Coordenada)) #confirm if instance belongs to class
    print(coord1._number) #try tomorrow to refactor to private and see if you can still use this expression to call private variable
  