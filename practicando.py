a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,4,5,6,7,8,9,10]

c=3

test=[]

for i in a:
    for x in b: 
      if i+x==c:
         par=(i,x)
         test.append(par)
         

print(test)
