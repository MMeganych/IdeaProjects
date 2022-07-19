# Усі Генератори - це також і ітератори

def my_function(x):
    return x


print(my_function(4))  # 4

# Ф-ція генератора _____________________


def count_up_to(x):
    count = 1
    while count <= x:
        yield count
        count += 1


print(count_up_to(4))     # <generator object count_up_to at 0x0000015F0AD59510>
counter = count_up_to(4)
# print(counter.__next__())  # 1
# print(counter.__next__())  # 2
# print(counter.__next__())  # 3
# print(counter.__next__())  # 4
# print(counter.__next__())  # StopIteration

print(next(counter))  # 1
print(next(counter))  # 2
counter1 = count_up_to(10)

# for number in counter1:
#  print(number)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

counter1.__next__()

for number in counter1:
    print(number)
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print(list(count_up_to(7)))          # [1, 2, 3, 4, 5, 6, 7]


def get_week_day():
    week_day_list = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday']
    for week_day in week_day_list:
        yield week_day


current_day = get_week_day()
print(current_day.__next__())     # 'Sunday'
print(current_day.__next__())     # 'Monday'
print(current_day.__next__())     # 'Tuesday'
print(current_day.__next__())     # 'Wednesday'
print(current_day.__next__())     # 'Thursday'
print(current_day.__next__())     # 'Friday'
print(current_day.__next__())     # 'Saturday'


def even_odd():
    while True:
        yield 'even'
        yield 'odd'


even_odd_generator = even_odd()
print(next(even_odd_generator))     # 'even'
print(next(even_odd_generator))     # 'odd'
print(next(even_odd_generator))     # 'even'
print(next(even_odd_generator))     # 'odd'
print(next(even_odd_generator))     # 'even'
print(next(even_odd_generator))     # 'odd'
print(next(even_odd_generator))     # 'even'
print(next(even_odd_generator))     # 'odd'
