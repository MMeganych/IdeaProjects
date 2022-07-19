for x in range(10):
    print(x)
# #0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
for x in range(3,10):
      print(x)
#  3
#  4
#  5
# 6
# 7
# 8
# 9

for x in range(3, 10, 2):
    print(x)    # krok cherez 2 elementa
# # 3
# # 5
# # 7
# # 9

letter_index = 0
my_string = 'adfagasg'
for letter in my_string:
     print(letter + ' is at index ' + str(letter_index))
     letter_index += 1
# a is at index 0
# d is at index 1
# f is at index 2
# a is at index 3
# g is at index 4
# a is at index 5
# s is at index 6
# g is at index 7

my_string = 'adfagasg'
for item in enumerate(my_string):
     print(item)
# (0, 'a')
# (1, 'd')
# (2, 'f')
# (3, 'a')
# (4, 'g')
# (5, 'a')
# (6, 's')
# (7, 'g')

my_string = 'adfagasg'
for index, letter in enumerate(my_string):
    print(letter + ' is at index ' + str(index))
# d is at index 1
# f is at index 2
# a is at index 3
# g is at index 4
# a is at index 5
# s is at index 6
# g is at index 7

print('a' in 'Jack')   # True
print('x' in 'Jack')   # False
print(str(1) in 'Jack')   # False
print('1' in 'Jack')   # False

letter_list = ['a', 'b', 'c']
print('a' in letter_list)  # True
print( 1 in letter_list)  # False

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(1 in dict_1)   # True
print(1 in dict_1.keys())   # True
print('z' in dict_1.values())   # False
print('c' in dict_1.values())   # True

print(min(1, 3, 56, 4 ))  # 1
print(max(1, 3, 56, 4 ))  # 56

my_list = [1, 3, 56, 4]
print(min(my_list))   # 1

print(max('Hello'))   # o

from random import shuffle
my_list = [1, 3, 56, 4]
shuffle(my_list)
print(my_list)  # [3, 56, 1, 4]

from random import randint
print(randint(1, 10))  # randomne chyslo ot 1 do 10

