# import random


# def busqueda_linal(list, objetivo):
#     match = False

#     for i in list:
#         if i == objetivo:
#             match = True
#             break

#     return match

# if __name__ == '__main__':
#     tamano_lista=int(input('De que tamano sera la lista? '))
#     objetivo=int(input('Que numero quieres encontrar? '))
#     lista=list(random.randint(1,100) for i in range(tamano_lista)) 
#     print(lista)
#     encontrado=busqueda_linal(lista, objetivo)
#     print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
   

import random

def busqueda_linear(list, objetivo):
    match=False
    for i in list:
        if i == objetivo:
            match=True        #aca se tiene que usar match y break si o si para parar el loop tan pronto se encuentro el objetivo en la lista
            break             #yo trate de no usar break y salia error porque retorba true y false en cada iteracion, se necesita un break y una variable
                              #que cambie a true cuando se encuentre el valor buscado
            
    return match

def run():
    tamano=int(input('Ingrese tamano: '))
    objetivo=int(input('Ingrese Objetivo: '))
    lista=list(random.randint(1,10) for i in range(tamano)) #aca randint coge un valor entre 1 y 10 y el for loop lo agrega a la lista tantas veces como indique el tamanho
    print(lista)                                            #Un enunciado podria ser esta funcion genera una lista de x terminos con valores random escogidos entre 1 e Y
    encontrado=busqueda_linear(lista, objetivo)
    print(encontrado)
    print(f'El numero {objetivo} {"si esta" if encontrado  else "no esta"} en la lista') #Sin estos ternary operators tendriamos que usar un if. aca es clave recordar que se usan " " dobles cuando se hace el if y tambien el orden dentro del if


if __name__=='__main__':
    run()
