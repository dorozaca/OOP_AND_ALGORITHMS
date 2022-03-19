# from ast import Break

# import random
# def lineal_search(list, target):
#     match=False
#     for i in list:
#         print(f'Looking for {target} between {i} and {list[-1:]}')
#         if i==target:
#             match=True
#             Break

#     return match

# def run():
#     target=int(input('Enter objective number: '))
#     size=int(input('Enter list size: '))
#     mylist=sorted(list(random.randint(0,20) for i in range(size)))
#     result=lineal_search(mylist, target)
#     print(f'The number {target} {"is" if result else "is not"} in the list')

# if __name__=='__main__':
#     run()

# import random
# def binary_search(list, target, high, low):
#     mid=low +(high-low)//2
#     counter=0
#     while low<=high:
#         print(f'Looking for {target} between {list[high]} and {list[low]}')
#         if list[mid]==target:
#             counter+=1
#             break
    
#         elif list[mid]>target:
#             high=mid-1

#         else:
#             low=mid+1

#         mid=low +(high-low)//2

#     if counter >0: 
#         return True
        
# def run():
    
#     target=int(input('Enter objective number: '))
#     size=int(input('Enter list size: '))
#     mylist=sorted(list(random.randint(1,20) for i in range(size)))
#     result=binary_search(mylist,target,len(mylist)-1,0)
#     print(f'The number {target}{" is" if result else "is not"} in list')
    

# if __name__=='__main__':
#     run()

import random
def recursive_binary(list, low, high,target):
    print(f'We are looking for {target} between {list[low]} and {list[high]}')
    if low>high:
        return False
    
    mid = (low + high)//2
    if list[mid]==target:
        return True
    
    elif list[mid]<target:
        return recursive_binary(list, mid+1,high,target)

    else:
        return recursive_binary(list, low, mid-1, target)

def run():
    size=int(input('Please enter size: '))
    target=int(input('Please enter target: '))
    mylist=sorted([random.randint(0,100) for i in range(size)])
    print(mylist)
    result=recursive_binary(mylist, 0, len(mylist)-1, target)
    print(f'The number {target} {"is" if result else "is not"} in list')

if __name__ == '__main__':
    run()
