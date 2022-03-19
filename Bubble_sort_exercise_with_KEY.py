def bubble_sort(list, key):
    
    n=len(list)

    for i in range(n-1,0,-1): #for i in range(n-1)
        ordered=False
        for j in range (i):      # for j in range(n-i-1)
            if list[j][key]>list[j+1][key]:
                list[j][key],list[j+1][key] = list[j+1][key],list[j][key]
                ordered=True
        if not ordered:
            break
    
    return list
    
def run():
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    print(bubble_sort(elements, key='transaction_amount'))
    print(bubble_sort(elements, key='name'))



if __name__ == '__main__':
    run()