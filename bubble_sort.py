

#My_bubble_sort_solution
import random
# def bubble_sort(list):
#     last_index=len(list)
      

#     for z in range(0,last_index-1):
#         for i in range(0,last_index):
#             if i == last_index-1:
#                 break
            
#             if list[i]>list[i+1]:
#                 list[i], list[i+1]=list[i+1], list[i]

#         last_index-=1
#     return list

       

# def run():
#     size=int(input('Please enter size: '))
#     mylist=([random.randint(0,100) for i in range(size)])
#     print(mylist)
    
#     sorted_list=bubble_sort(mylist)
#     print(sorted_list)

# if __name__ == '__main__':
#     run()

import random
def bubble_sort(list):
   n=len(list)

   for i in range(n):
       for j in range(n-1-i):
           print (f'i = {i} and j ={j}')
           if list[j]>list[j+1]:
            list[j], list[j+1]=list[j+1], list[j]  

    # for i in range(len(list)-1,0,-1):
    #     for j in range(0,i):
    #         if list[j]>list[j+1]:
    #             list[j], list[j+1]=list[j+1], list[j] 


   return list
       

def run():
    size=int(input('Please enter size: '))
    mylist=([random.randint(0,100) for i in range(size)])
    print(mylist)
    sorted_list=bubble_sort(mylist)
    print(sorted_list)

if __name__ == '__main__':
    run()
