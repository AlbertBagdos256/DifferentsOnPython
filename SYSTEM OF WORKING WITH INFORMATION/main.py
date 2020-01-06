#Algoritms of creating,sorting and finding element of massive
#-------------------------#
#Author: Albert Bagdasarov
#Date: 20.10.19 0:40
#-------------------------#

#Getting massive
print('Enter the amount of elements wich you need')
times = int(input())
i=0
my_list = []
while i < times:
    elements = int(input())
    i+=1
    my_list.append(elements)
    if i == times:
        print(my_list)

#Sorting elements of massive
def buble_sort(list1):
    amount = len(list1)-1
    for i in range(0,amount):
        for x in range(0,amount):
            if list1[x] > list1[x+1]:
                list1[x],list1[x+1] = list1[x+1],list1[x]
    return list1
print()
print('old_list',my_list)
new_list = buble_sort(my_list).copy()
print()
print('new_list',new_list)
#Finding the elements from the massive

def bynary_search(list,item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = (low+high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
            return None
print()
print('enter element which you want to find')
items = int(input())            
print('the index of your element is ' + str(bynary_search(my_list,items)) )    
                    