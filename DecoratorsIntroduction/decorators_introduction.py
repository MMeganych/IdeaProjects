def simple_function():
    print('Simple function code')

simple_function()     # Simple function code


def decorator_function(original_function):
    def wrap_function():
        print('Some code before the old code')
        original_function()
        print('Some code after the old code')
    return wrap_function()


#decorated_function = decorator_function(simple_function)

#decorated_function   # Some code before the old code
#                        Simple function code
#                        Some code after the old code


@decorator_function
def simple_function():
    print('Simple function code')


# ----------------------------------------------------------


def make_compliment(func):
    def wrapper():
        print('Nice to meet you!')
        func()
        print('You look great!')
    return wrapper()


@make_compliment
def ask_name():
    print('What is you name?')
# Nice to meet you!
# What is you name?
# You look great!


# ------------------------------------------
def make_compliment1(func):
    def wrapper(*args, **kwargs):
        print('Nice to meet you!')
        func(*args, **kwargs)
        print('You look great!')
    return wrapper


@make_compliment1
def ask_name():
    print('What is your name?')


ask_name()


@make_compliment1
def say_name(name):
    print('My name is ' + name)


say_name('Jack')


@make_compliment1
def order(food, drink):
    print(f'Give me {food} and {drink}')


order(food='chips', drink='kola')


