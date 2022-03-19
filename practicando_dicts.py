# a = [1,2,3,4,5,6,7,8,9,10]
# b = [1,2,3,4,5,6,7,8,9,10]

# c=3

# test=[]

# for i in a:
#     for x in b: 
#       if i+x==c:
#          par=(i,x)
#          test.append(par)
         

# print(test)

# from collections import namedtuple
# from typing import Counter 
# Color=namedtuple('Color',['azul','rojo','amarillo'])
# white=Color(25,76,18)

# print(white.azul)

# mycollect=[12,12,12,55,55,55,55,66,66,66,77,77,78,79,79,21,21,21,21,21,21,33,33,33,]
# y=Counter(mycollect)
# print(y)
# print(y.most_common(1))

# from operator import itemgetter


# mylistoftuple=[('w',30),('t',17),('g',22),('l',4),('r',12),('p',8),('x',7),('a',15),('z',10),]
# y=sorted(mylistoftuple,key=itemgetter(0))
# print(y)



thisdict = {
  "brand": 454,
  "electric": 200,
  "year": 196,
  "colors": 5000,
  'Toyota':9000
}

for i in thisdict:
  print(i,thisdict[i])

for i,j in thisdict.items(): #modificar valores durante iteracion
  thisdict[i]=j*0.9          #no olvidar usar thisdict[i]

print(thisdict.items())

for i,j in list(thisdict.items()): #eliminar elemento por llave
  if i == 'Toyota':
    del thisdict[i]

print(thisdict.items())

print(180 in thisdict.values())
print(('year',176.4) in thisdict.items()) #cuando queremos usar membership test con .items() necesitamos poner key and values en tuplas

thisdict['Chevy']=5000 #asi se agrega elemento a dictionary / tuple add no existe hay que convertirla a list // list si usa appened
print(thisdict.items())

dict2={}   #invertir llaves y valores usando segundo diccionario
for i,j in thisdict.items():
  dict2[j]=i
print(dict2.items())

dict3={}   #filtrar por valor y agregar a segundo diccionario
for i,j in thisdict.items():
  if j <250:
    dict3[i]=j # esta es la clave para clonar items que cumplen la condicion

print(dict3.items())

ventas={'Enero':500, 'Febrero':800, 'Marzo':1350, 'Abril':1500, 'Mayo':1700}

container=0
for values in ventas.values(): #solo funciona con .value()
  container+=values

print(values)


  



