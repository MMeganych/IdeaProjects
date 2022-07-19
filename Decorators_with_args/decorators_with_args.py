from functools import wraps


def check_if_first_args_is(value):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args and args[0] != value:
                print(f'First argument has to be {value}')
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@check_if_first_args_is('red')
def print_rainbow_colors(*colors):
    print(colors)


print_rainbow_colors('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
# ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')

print_rainbow_colors('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
# First argument has to be red
# ('orange', 'yellow', 'green', 'blue', 'indigo', 'violet')


@check_if_first_args_is(7)
def multiply_7(a, b):
    return a * b


print(multiply_7(8, 3))
# First argument has to be 7
# 24

print(multiply_7(7, 3))  # 21


# -------------------------------------------------------------------------------------------------
def enforce(*types):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            new_args = []
            for a, t in zip(args, types):
                new_args.append(t(a))
            return func(*new_args, **kwargs)
        return wrapper
    return inner_dec


def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', 3)
# Hi!
# Hi!
# Hi!

# print_text_n_times('Hi!', '3')  # TypeError: 'str' object cannot be interpreted as an integer


# ------------------------------------------------------------------------------------------------
@enforce(str, int)
def print_text_n_times(text, n):
    for number in range(n):
        print(text)


print_text_n_times('Hi!', '3')
# Hi!
# Hi!
# Hi!

# *args - ('Hi!' , '3')
# *types - (srt, int)
# zip(args, types) - ('Hi!', str) ('3', int)


# ---------------------------------------------------------------------------------------------------------
def divide(a, b):
    return a / b


print(divide(4, 2))  # 2.0
# print(divide('4', '2'))  # TypeError: unsupported operand type(s) for /: 'str' and 'str'


@enforce(float, float)
def divide(a, b):
    return a / b


print(divide(4, 2))      # 2.0
print(divide('4', '2'))  # 2.0

# -------------------------------------------------- D Z -------------------------------------------------------

from time import sleep


def wait(n):
    def inner_dec(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sleep(n)
            print(f"There was a pause {n} seconds before execution {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return inner_dec


@wait(5)
def divide(a, b):
    return a / b


print(divide(4, 2))
# There was a pause 5 seconds before execution divide
# 2.0



