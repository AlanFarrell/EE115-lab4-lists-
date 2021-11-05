import random
from random import randint
'''
create an empty list
create a while loop
each time the while loop goes around append this empty list 
keep going until this loops 10 times 
'''
#method 1
list = []# creating an empty list
while len(list) < 10: #capping how many times the append can loop
    list.append(random.randint(0,100)) #append is adding a digit to the list each time it loops
list.sort() #sorting the list from lowest to largest
print(list)


#method 2

list = [random.randint(0, 100) for i in range(10)]
print(list)




