import random
from random import randint
'''
import our q3 code
apply a condition to our nums in a list 
use for loop 
condition = if num divides by 2 then its even
set condition so that if it isnt divisable by two then that it what gets printed
'''

list = []# creating an empty list
while len(list) < 10: #capping how many times the append can loop
    list.append(random.randint(0,100)) #append is adding a digit to the list each time it loops
for num in list:
    if num % 2 != 0: #this is a condition check to find odd numbers
        print(num)
