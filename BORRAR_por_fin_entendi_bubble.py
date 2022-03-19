import random
def bubble_sort(list):
   n=len(list)
   for i in range(n): #me av a recorrer cada uno de los elementos pero llamandolos por sus indices
       print(f'i={i}')
       for j in range(n-i-1): #luego me va hacer la comparacion pero evitando los elementos k ya estan ordenados en los previos pases, por eso (-i) tambien va menos 1 porque
           print(f'i={i} and j={j}')
           if list[j]>list[j+1]: #debemos solo debems aplicar la comparacion el penultimo elemento de cada pase (porque si no el ultimo no tendria con quien comparar porque ya no hay nadie mas adelante)
              list[j],list[j+1]=list[j+1], list[j]
           print(list)

   return list

# def bubble_sort(list):
#    n=len(list)
#    for i in range(n-1,0,-1): #aca trabajamos con indices, por eso va (n-1) como paso inicial
      
#        for j in range(i): 
#            if list[j]>list[j+1]: 
#             list[j],list[j+1]=list[j+1], list[j]

#    return list


   
       

def run():
    size=int(input('Please enter size: '))
    mylist=([random.randint(0,100) for i in range(size)])
    print(mylist)
    sorted_list=bubble_sort(mylist)
    print(sorted_list)

if __name__ == '__main__':
    run()
