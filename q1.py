'''
we create a list (my_list)
add a counter
while count is less than the number of ints in my_list
print a single value in my_list

'''

my_list = [1, 2, 3, 5, 7, 11, 13, 17]
print(my_list)

count = 0
while int(count) < len(my_list): #counting length of our list
    for num in my_list: #using for loop to increment what we are printing
        print(num)
        print() #printing a space for extra readability when it is printed to terminal
    count = count + 1
