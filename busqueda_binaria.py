#import random

# def lineal_search(list, target):
#     match=False

#     for i in list:
#         if i == target:
#             match=True
#             break

#     return match
    

# def run():
#     target=int(input('What number you are looking for? '))
#     size=int(input('What length you prefer the list? '))

#     mylist=list(random.randint(1,10) for i in range(size))
#     print(mylist)

#     search_result=lineal_search(mylist, target)
#     print(f'The number {target} {"is" if search_result else "is not"} in the list')

# if __name__== '__main__':
#     run()



# import random

# def binary_search(list,target, start, stop):
    
#     print(f'Looking for {target} between {list[start]} and {list[stop]}')
#     counter=0
#     mid=start+(stop-start)//2
#     while start <= stop:
#         

#         if target==list[mid]:
#             counter+=1
#             break
            
#         elif target>list[mid]:
#             start=mid+1
            

#         else:
#             stop=mid-1
            
#         mid=start+(stop-start)//2

#     if counter>0:
#         return True

             

# def run():
#     target=int(input('What number you are looking for? '))
#     size=int(input('What length you prefer the list? '))

#     mylist=sorted(list(random.randint(1,100) for i in range(size)))
#     print(mylist)

#     search_result=binary_search(mylist,target, 0, (len(mylist)-1))
#     print(f'The number {target} {"is" if search_result else "is not"} in the list')

# if __name__== '__main__':
#     run()


import random

def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 10) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(encontrado)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')