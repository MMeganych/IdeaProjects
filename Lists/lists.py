# number_list = [32, 21, 48, 34.56]
# print(number_list)
# some_list = [12,35.334, 'hello']
# print(some_list)
# print(len(some_list))             # 3
# print(some_list[1])               # 35.334
# another_list = some_list[:2]
# print(another_list)                # [12, 35.334]
# some_list[2] = 'hi'
# print(some_list)                    # [12, 35.334, 'hi']
# new_list = some_list + another_list
# print(new_list)                   # [12, 35.334, 'hi', 12, 35.334]

  # Adding items

#new_list[5] = 'new item'
# print(new_list)                        # IndexError: list assignment index out of range
#
# new_list.append('new item')           # метод .append( ) добавляє новий елемент в кінець списку
# print(new_list)                     # [12, 35.334, 'hi', 12, 35.334, 'new item']
#
# new_list.insert(0, 'start')            # метод .insert() добавляє новий елемент на початок списку, тобто нульовий
# print(new_list)                    # ['start', 12, 35.334, 'hi', 12, 35.334, 'new item']
#
# new_list.insert(2, 13)                # вставляємо число "13" як другий елемент у списку
# print(new_list)                       # ['start', 12, 13, 35.334, 'hi', 12, 35.334, 'new item']
#
#   # Removing items
#
# # new_list.pop()               # метод .pop( ) видаляє останній елемент з кінця списку
# # # new_list.pop(-1)             #  також видаляє останній елемент з кінця списку
# # print(new_list)              # ['start', 12, 13, 35.334, 'hi', 12, 35.334]
# #
# # new_list.pop(0)               # метод .pop( ) видаляє перший елемент зi списку
#                               # [12, 35.334, 'hi', 12, 35.334, 'new item']
#
# deleted_item = new_list.pop()  # тут останній видалений елемент повернуто і поміщенно в перемінну "deleted_item"
# print(new_list)                # ['start', 12, 13, 35.334, 'hi', 12, 35.334]
# print(deleted_item)            # new item
#
# my_list.pop(1) = new_list.pop(-3) # тут видалений елемент "hi" повернуто і поміщенно в перемінну "deleted_item"
# print(new_list)                # ['start', 12, 13, 35.334, 12, 35.334]
# print(deleted_item)            # hi
#
# deleted_item =  new_list.remove(12)  # метод .remove() видаляє не по індексу елемент, а за значенням (12)
#  і нічого він вже не поверне нам
# print(new_list)                # ['start', 13, 35.334, 12, 35.334]
# print(deleted_item)            # None

number_list = [45, 12, 3, -455, 22]
letter_list = ['s', 'w', 't', 'a']
print(number_list)     # [45, 12, 3, -455, 22]
print(letter_list)     # ['s', 'w', 't', 'a']

number_list.sort()     # метод .sort() відсортує числа від найменшого до найбільшого і нічого він вже не поверне нам
letter_list.sort()     # метод .sort() відсортує букви за алфавітом і нічого він вже не поверне нам
print(number_list)     # [-455, 3, 12, 22, 45]
print(letter_list)     # ['a', 's', 't', 'w']

number_list.reverse()  # метод .reverse() відсортує числа від найбільшого  до найменшого і нічого він вже не поверне нам
letter_list.reverse()  # метод .reverse() відсортує букви за алфавітом в зворотньому порядку і нічого він вже не поверне нам
print(number_list)     # [45, 22, 12, 3, -455]
print(letter_list)     # ['w', 't', 's', 'a']

number_list.append(letter_list)
print(number_list)  # [45, 22, 12, 3, -455, ['w', 't', 's', 'a']]

my_list = [134.5862, 89, 'lessons 18', 'yes', 139, 'Elon Musk']
my_new_list = my_list[1:4]
print(my_new_list)





