# print("Hello, world! This is my name: Hailey Wilson")

# name = input('What is your name?\n')
# print ('Hi, %s.' % name)

# friends = ['John B', "Pope", 'JJ', 'Kiera', 'Sara', 'Topper']
# for i, name in enumerate(friends):
#    print("iteration {iteration} is {name}".format(iteration=i, name=name))

# parents, babies = (1,1)
# while babies<100:
#    print('This generation has {0} babies'.format(babies))
#    parents, babies = (babies, parents+babies)

# def greet(name):
#    print('Hello, ', name)
# greet('John B')
# greet('JJ')
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

mylist = [1, 2, 3]
print(mylist[2])

numbers = [1, 3, 5, 7, 9]
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

lotsofhellos = "hello" * 10
print(lotsofhellos)

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)

# Python program to print Even Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

