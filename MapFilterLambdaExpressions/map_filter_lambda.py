# Map
def sum_of_two_numbers(x):
    return x + x


number_list = [1, 2, 3, 4, 5, 6, 7]

result = map(sum_of_two_numbers, number_list)   # тут поміщаємо ф-цію без скобок
print(result)   # <map object at 0x000002B4BF02DC40>

for item in result:
    print(item)
# 2
# 4
# 6
# 8
# 10
# 12
# 14

for item in map(sum_of_two_numbers, number_list):
    print(item)
# 2
# 4
# 6
# 8
# 10
# 12
# 14

print(list(map(sum_of_two_numbers, number_list)))    # [2, 4, 6, 8, 10, 12, 14]


def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False


string_list = ['hi', 'was', 'name', 'he' ]
print(list(map(is_a_in_string, string_list)))      # тут поміщаємо ф-цію без скобок
# String has not "a"
# String has "a"
# String has "a"
# String has not "a"
# [False, True, True, False]


# Filter  (повертає тільки значення True або False )
def is_number_odd(number):
    return  number % 2 == 1


number_list = [1, 2, 3, 4, 5, 6, 7]

print(filter(is_number_odd, number_list))        # <filter object at 0x00000207710BFB20>
print(list(filter(is_number_odd, number_list)))  # [1, 3, 5, 7]

for number in filter(is_number_odd, number_list):
    print(number)
# 1
# 3
# 5
# 7

def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False


string_list = ['hi', 'was', 'name', 'he' ]
print(list(filter(is_a_in_string, string_list)))


# Lambda Expression
def cube(number):
    return number ** 3


number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(cube, number_list)))   # [1, 8, 27, 64, 125, 216, 343]

print(list(map(lambda number: number ** 3, number_list)))   # [1, 8, 27, 64, 125, 216, 343]
string_list = ['hi', 'was', 'name', 'he']
print(list(map(lambda string: string[-1], string_list)))    # ['i', 's', 'e', 'e']
print(list(map(lambda string: string[::-1], string_list)))  # ['ih', 'saw', 'eman', 'eh']

print(list(filter(lambda number: number % 2 == 1, number_list)))  # [1, 3, 5, 7]
print(list(filter(lambda number: number % 2 == 0, number_list)))  # [2, 4, 6]