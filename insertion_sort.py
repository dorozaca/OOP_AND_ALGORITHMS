import random
def insertion_sort(list):

    for i in range(1,len(list)):
        while list[i-1]>list[i] and i>0:
            list[i],list[i-1]=list[i-1],list[i]
            i-=1
    return list


lista=[random.randint(1,50) for i in range (20)]
lista2=list(i for i in range(50))
print(lista)
print(lista2)
print(insertion_sort(lista))