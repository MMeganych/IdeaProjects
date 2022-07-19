number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in number_list:
    print(str(number) + 'Hola!')
    print('Hola!')
# 1Hola!
# Hola!
# 2Hola!
# Hola!
# 3Hola!
# Hola!
# 4Hola!
# Hola!
# 5Hola!
# Hola!
# 6Hola!
# Hola!
# 7Hola!
# Hola!
# 8Hola!
# Hola!
# 9Hola!
# Hola!
# 10Hola!
# Hola!

for number in number_list:
     if number % 2 == 0:
         print(number)
     else:
         print('Hey!')
# Hey!
# 2
# Hey!
# 4
# Hey!
# 6
# Hey!
# 8
# Hey!
# 10

list_numbers_sum = 0
for number in number_list:
    list_numbers_sum = list_numbers_sum + number
print(list_numbers_sum)   #55

greeting = 'Hello Python!'
for letter in greeting:
    print(letter)
# H
# e
# l
# l
# o
#
# P
# y
# t
# h
# o
# n
# !
#

greeting = 'Hello Python!'
for letter in greeting:
    if letter == 'o':
        print(letter)
# o
# o

greeting = 'Hello Python!'
for letter in greeting:
    if letter != 'o':
        print(letter)
# H
# e
# l
# l
#
# P
# y
# t
# h
# n
# !

for letter in 'Hello Python!':
    if letter != 'o':
        print(letter)
# H
# e
# l
# l
#
# P
# y
# t
# h
# n
# !

for letter in 'Hello Python!':
     print('One more letter!')
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!
# One more letter!

tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)
# ('a', 'b')
# ('c', 'd')
# ('e', 'f')

tuple_list = [('a', 'b'), ('c', 'd'), ('e', 'f')]
for item in tuple_list:
    print(item)
for letter_1, letter_2 in tuple_list:
    print(letter_1, letter_2)
# a b
# c d
# e f

tuple_list_1 = [('a', 'b', 1), ('c', 'd', 4), ('e', 'f', 5)]
for letter_1, letter_2, number in tuple_list_1:
    print(letter_1, letter_2, number)
# a b 1
# c d 4
# e f 5

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary:
    print(item)
# key1
# key2
# key3

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary.keys():
    print(item)
# key1
# key2
# key3

dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary.items():
    print(item)
# ('key1', 'value1')
# ('key2', 'value2')
# ('key3', 'value3')


dictionary = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
for item in dictionary.values():
    print(item)
# value1
# value2
# value3

for x in range(5):
    print(x)
# 0
# 1
# 2
# 3
# 4

for x in range(5):
    print('Hello!')
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!

for _ in range(5):
    print('Hello!')
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!

number_10_30 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
sum_n = 0
for number in number_10_30:
    if number % 2 == 0:
        sum_n = sum_n + number
print(sum_n)

input_number = int(input('Enter number: '))
for _ in range(input_number):
    print('Hello!')

