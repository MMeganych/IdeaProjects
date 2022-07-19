from time import time
from functools import wraps


def speed_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        end_time = time()
        print(f'Time of code execution {end_time - start_time}')
        return result
    return wrapper


@speed_test
def sum_with_list():
    return sum([number for number in range(100000)])


@speed_test
def sum_with_gen():
    return sum(number for number in range(100000))


@speed_test
def product(range_value):
    result = 1
    for number in range(1, range_value):
        result *= number
    return result


print(sum_with_list())   # Time of code execution 0.005536079406738281
#                          4999950000

print(sum_with_gen())   # Time of code execution 0.013559103012084961
#                          4999950000

print(product(10000))


# ------------------------------------------- D Z ----------------------------------------------------------

def hello_from_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return str(result) + ' Hello from decorator!'
    return wrapper


@hello_from_decorator
def sum1(a):
    return a + a + 4


print(sum1(5))    # 14 Hello from decorator!


