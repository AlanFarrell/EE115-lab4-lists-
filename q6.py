import random
from random import randint
'''
import q3 
use sum fucntion 
print the sum of the list 
'''


list = []# creating an empty list
while len(list) < 10: #capping how many times the append can loop
    list.append(random.randint(0,100)) #append is adding a digit to the list each time it loops
print(list)
print(sum(list))