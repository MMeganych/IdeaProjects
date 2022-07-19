def get_number_from_range():
    for number in range(10):
        yield number


counter = get_number_from_range()
print(next(counter))    # 0
print(next(counter))    # 1
print(next(counter))    # 2
print(next(counter))    # 3
print(next(counter))    # 4
print(next(counter))    # 5
print(next(counter))    # 6
print(next(counter))    # 7
print(next(counter))    # 8
print(next(counter))    # 9
# print(next(counter))    # StopIteration

# ______________________ Generator expressions ______________________________

counter1 = (number for number in range(10))    # - тiльки тут круглi скобки
print(next(counter1))   # 1
print(next(counter1))   # 2
print(next(counter1))   # 3
print(next(counter1))   # 4
print(next(counter1))   # 5
print(next(counter1))   # 6
print(next(counter1))   # 7
print(next(counter1))   # 8
print(next(counter1))   # 9
# print(next(counter1))   # StopIteration
