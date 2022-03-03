class Coordenada:
    def __init__(self, x, y, number) :
        self.x=x
        self.y=y
        self.__number=number

        @property
        def Number(self):
            return self.__number

        @Number.setter #it seems like we can use lower case here
        def Number(self,value):
            self.__number=value

    @staticmethod
    def my_method():
        print('La hiciste')


    def distancia(self, second_coordenada):
        x_diff=(self.x-second_coordenada.x)**2
        y_diff=(self.y-second_coordenada.y)**2

        return (x_diff-y_diff)**0.5

if __name__== '__main__':
    coord1=Coordenada(10,50,40)
    coord2=Coordenada(5,40,20)

    print(vars(coord1))
    print(coord1.distancia(coord2))     #callling another instance within a methon
    coord1.Number=30
    coord1.Number=100
    container=coord1.Number
    print(f'My nombre es {coord1.Number}')
    print(vars(coord1))
    print(isinstance(coord1, Coordenada)) #confirm if instance belongs to class
  