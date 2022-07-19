# --------------------------- *args -----------------------------------------------------------
def ten_percent_of_product(x, y):
    return (x * y) * 0.1


print(ten_percent_of_product(10, 20))     # 20.0


def ten_percent_of_product(x, y, z):
    return (x * y * z) * 0.1


print(ten_percent_of_product(10, 20, 7))     # 140.0


def func_with_args(*args):
    print(args)


func_with_args(10, 20, 7)     # (10, 20, 7)


def ten_percent_of_product_with_args(*args):
    product = 1
    for number in args:
        product = product * number
    return product * 0.1


print(ten_percent_of_product_with_args(10, 20))     # 20.0


def ten_percent_of_product_with_args(percent, *args):
    product = 1
    for number in args:
        product = product * number
    return product / 100 * percent


print(ten_percent_of_product_with_args(10, 10, 20))     # 20.0
print(ten_percent_of_product_with_args(20, 10, 20))     # 40.0


#  **kwargs / ключ повинен бути записаний тільки строкою, а не цифрою

def func_with_kwargs(**kwargs):
    print(kwargs)


func_with_kwargs(first=1, second=2, third=3)   # {'first': 1, 'second': 2, 'third': 3}


def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print("Hello! Nice to meet you, {}".format(kwargs['name']))
    else:
        print('Hello! What is your name?')


hello_with_kwargs(gender='male', age=24, name='Jack')  # Hello! Nice to meet you, Jack
hello_with_kwargs(gender='male', age=24)  # Hello! What is your name?


def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print("{}! Nice to meet you, {}".format(greeting, kwargs['name']))
    else:
        print('{}! What is your name?'.format(greeting))


hello_with_greeting_and_kwargs('Hi', gender='male', age=24, name='Jack')  # Hi! Nice to meet you, Jack


def func_with_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')
# ('one', 'two')
# {'drink': 'coffee', 'food': 'sandwich'}


def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


func_with_args_and_kwargs('one', 'two', drink='coffee', food='sandwich')    # I would like one sandwich

# -------- d z ------------------------


def is_cat_here(*args):
    if 'cat' in args:
        return True
    elif 'Cat' in args:
        return True
    else:
        return False


print(is_cat_here('Dakota', 'vine', 'dog', 'cat', 'sandwich'))


def is_item_here(item, *args):
    return item in args


print(is_item_here(10, 10, 60, 456, 15))


def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}, what is your favorite color?'.format(my_color))


your_favorite_color('yellow', drink='coffee', name='Jack', color='red', age=29, car='Seat')
# My favorite color is yellow, but red is also pretty good!

your_favorite_color('yellow', drink='coffee', name='Jack',  age=29, car='Seat')
# My favorite color is yellow, what is your favorite color?

