def squares_sum(a, b):
    '''

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    '''
    return a * a + b * b


print(squares_sum(2, 3))               # 13

print(squares_sum.__doc__)             # :param a: first number
#                                        :param b: second number
#                                        :return: sum of squares first and second numbers: (a * a + b * b)

print(squares_sum.__name__)            # squares_sum


from functools import wraps


# створимо декоратор який буде описувати попередню ф-цію
def print_function_data(function):
    '''
    This is decorator function
    :param function:
    :return:
    '''
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f'You are using:  {function.__name__}')
        print(f'Function documentation: {function.__doc__}')
        return function(*args, **kwargs)
    return wrapper


@print_function_data
def squares_sum(a, b):
    '''

    :param a: first number
    :param b: second number
    :return: sum of squares first and second numbers: (a * a + b * b)
    '''
    return a * a + b * b


print(squares_sum(2, 3))               # You are using:  squares_sum
#                                        Function documentation:

#                                            :param a: first number
#                                            :param b: second number
#                                            :return: sum of squares first and second numbers: (a * a + b * b)

#                                          13

# ----------------------------------------------------------------------------------------------------------------

print(squares_sum.__doc__)      # None
print(squares_sum.__name__)     # wrapper
help(squares_sum)               # Help on function wrapper in module __main__:
#                                 wrapper(*args, **kwargs)

# ----------------------------  @wraps --------------------------------------

print(squares_sum.__doc__)             # :param a: first number
#                                        :param b: second number
#                                        :return: sum of squares first and second numbers: (a * a + b * b)
print(squares_sum.__name__)            # squares_sum

help(squares_sum)      # Help on function squares_sum in module __main__:

#                        squares_sum(a, b)
#                            :param a: first number
#                            :param b: second number
#                            :return: sum of squares first and second numbers: (a * a + b * b)


# ---------------------------------------- D Z -----------------------------------------------

def print_args(function):
    '''
    А function that prints the arguments of the * args and ** kwargs functions that it decorates
    :param function:
    :return:
    '''
    def wrap(*args, **kwargs):
        print(f'Argument *args: {args}')
        print(f'Argument **kwargs: {kwargs}')
        return function(*args, **kwargs)
    return wrap


@print_args
def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

# Argument *args: ('one', 'two')
# Argument **kwargs: {'drink': 'coffee', 'food': 'sandwich'}


func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')   # I would like one sandwich





