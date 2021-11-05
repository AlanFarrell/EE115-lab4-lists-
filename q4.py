import random
from random import randint
'''
using same process as before we find 10 random ints
find largest(max function)
print list
print max/max location in list 

'''

list = []# creating an empty list
while len(list) < 10: #capping how many times the append can loop
    list.append(random.randint(0,100)) #append is adding a digit to the list each time it loops
max = max(list)
print(list)
print(max)
print(f"the max value is at the index {list.index(max)}")

