# Iterate

# Iterables objects

number_list = [1, 2, 3, 4, 5]

for number in number_list:
    print(number)

for letter in 'my string':
    print(letter)

# Iterators

number_list_iterator = iter(number_list)
print(type(number_list_iterator))            # <class 'list_iterator'>


string_iterator = iter('my string')
print(type(string_iterator))                 # <class 'str_iterator'>

print(number_list_iterator.__next__())        # 1
print(number_list_iterator.__next__())        # 2
print(number_list_iterator.__next__())        # 3
print(number_list_iterator.__next__())        # 4
print(number_list_iterator.__next__())        # 5
# print(number_list_iterator.__next__())      # StopIteration

print(string_iterator.__next__())              # m
print(string_iterator.__next__())              # y

# iter(1)                                   # TypeError: 'int' object is not iterable

print(next(number_list_iterator))              # 1
print(next(number_list_iterator))              # 2
print(next(number_list_iterator))              # 3
print(next(number_list_iterator))              # 4
print(next(number_list_iterator))              # 5
# print(next(number_list_iterator))              # StopIteration


def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            break


my_for_loop('gears 5')
# g
# e
# a
# r
# s
#
# 5
my_for_loop([1, 2, 3, 4, 5])
# 1
# 2
# 3
# 4
# 5

