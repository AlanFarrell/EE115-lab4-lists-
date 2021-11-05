'''
we create a list (my_list)
reverse the list using reverse function
add a counter
while count is less than the number of ints in my_list
we print out our first list reversed
then we print a single value of the reversed list per line

'''

my_list = [1, 2, 3, 5, 7, 11, 13, 17]
my_list.reverse() #reversing the list
print(my_list)

count = 0
while int(count) < len(my_list): #counting length of our list
    for num in my_list: #using for loop to increment what we are printing
        print(num)
        print() #printing a space for extra readability when it is printed to terminal
    count = count + 1

