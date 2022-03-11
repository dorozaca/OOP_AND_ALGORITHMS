class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def area(self):               #este punto es clave porque solo paso el objeto
        return self.base * self.altura #y aca trabajo con las propiedades que el objeto ya debe tener incorporadas desde su construccion arribva

class Cuadrado(Rectangulo):
    def __init__(self, lado): 
        super().__init__(lado, lado) #aca no necesito usar exactamente los nombres de los atribuitos de la clase padre que estamos invocando. Solo tenemos que cumplir con pasar dos argumentos


mirectangulo = Rectangulo(10,5)
micuadrado = Cuadrado(3)
print(mirectangulo.area())
print(micuadrado.area())