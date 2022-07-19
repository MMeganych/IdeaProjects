# Infinite process

def create_patterns():
    max_patterns = 100
    patterns = ('First pattern', 'Second pattern',
                'Third pattern', 'Forth pattern')
    i = 0
    result_list = []
    while len(result_list) < max_patterns:
        if i >= len(patterns):
            i = 0
        result_list.append(patterns[i])
        i += 1
    return result_list


print(create_patterns())         # ['First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern',
# 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern',
# 'Third pattern', 'Forth pattern', 'First pattern', 'Second pattern', 'Third pattern', 'Forth pattern']


# ----------------------------------------------------------------------------------------------------
def get_current_pattern():
    patterns = ('First pattern', 'Second pattern',
                'Third pattern', 'Forth pattern')
    i = 0
    while True:
        if i >= len(patterns):
            i = 0
        yield patterns[i]
        i += 1


current_pattern = get_current_pattern()
print(current_pattern.__next__())         # First pattern
print(current_pattern.__next__())         # Second pattern
print(current_pattern.__next__())         # Third pattern
print(current_pattern.__next__())         # Forth pattern
print(current_pattern.__next__())         # First pattern
print(current_pattern.__next__())         # Second pattern


# Создайте функцию, возвращающую генератор, бесконечно вырабатывающий квадраты целых чисел, начиная с 1

def get_infinite_square_generator():
    i = 1
    while True:
        yield i*i
        i += 1


infinite_square_generator = get_infinite_square_generator()
print(next(infinite_square_generator))     # 1
print(next(infinite_square_generator))     # 4
print(next(infinite_square_generator))     # 9
print(next(infinite_square_generator))     # 16
print(next(infinite_square_generator))     # 25
print(next(infinite_square_generator))     # 36

