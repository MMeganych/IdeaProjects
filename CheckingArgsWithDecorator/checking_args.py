from functools import wraps


def prohibit_kwargs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('Keyword arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


@prohibit_kwargs
def print_hello(name):
    print(f'Hello {name}!')


print_hello('Jack')       # Hello Jack!

#print_hello(name='Jack')  # ValueError: Keyword arguments are prohibited


def prohibit_int_arguments(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for val in args:
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        for key, val in kwargs.items():
            if type(val) == int:
                raise ValueError('Integer arguments are prohibited')
        return func(*args, **kwargs)
    return wrapper


@prohibit_int_arguments
def print_hello(name):
    print(f'Hello {name}!')


print_hello('Jack')       # Hello Jack!
#print_hello(3)    # ValueError: Keyword arguments are prohibited


# ------------------------------------------------------- D Z ---------------------------------------------------------

def prohibit_more_than_2_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if len(args) > 2:
            raise ValueError('Function must have less than 3 arguments!')
        if len(kwargs) > 2:
            raise ValueError('Function must have less than 3 arguments!')
        return func(*args, **kwargs)
    return wrapper


@prohibit_more_than_2_args
def func_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


func_with_args_and_kwargs('one', 'two', hot='tea', drink='coffee', food='sandwich')
# ValueError: Function must have less than 3 arguments!

func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')
# ('one', 'two')
# {'drink': 'coffee', 'food': 'sandwich'}

func_with_args_and_kwargs('one', 'two', 'third', drink='coffee', food='sandwich')
# ValueError: Function must have less than 3 arguments!