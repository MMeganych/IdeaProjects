# ----------------- Higher order functions, which accept another functions as arguments --------------------
# ----------------- Функції вищого порядку, які приймають інші функції як аргументи ------------------------


def product(n, func):
    result = 1
    for number in range(1, n):
        result *= func(number)
    return result


def square(x):
    return x * x


def cube(x):
    return x * x * x


print(product(4, square))       # 36

print(product(4, cube))         # 216


def my_function(a, b, func):
    result = func([a, b])        # тут краще передати параметри в формі списку [] , щоб вони були iterable
    return result


print(my_function(2, 3, sum))     # 5


# Using nested functions


from random import choice


def colorize(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    result = get_color() + ' ' + thing
    return result


print(colorize('apple'))  # green apple
print(colorize('apple'))  # red apple
print(colorize('apple'))  # red apple

# --------------- Higher order functions, which return another function --------------------------
# --------------- Функції вищого порядку, які повертають іншу функцію ----------------------------


def make_color():
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color

    return get_color


first_color = make_color()
print(first_color())                  # red

# first_color() - можемо в кінці цієї перемінної дописати скобки, бо в ній зберігається ф-ція get_color()

second_color = make_color()
print(second_color())                  # green

third_color = make_color()
print(third_color())                   # red

# ------------------- Inner functions can access outer function scope ----------------------------------------
# ------------------- Внутрішні функції можуть отримати доступ до зовнішньої області функції -----------------


def colorize1(thing):
    def get_color():
        colors = ('red', 'green', 'yellow')
        color = choice(colors)
        return color + ' ' + thing

    return get_color


print(colorize1('apple')())               # yellow apple
colorized_dog = colorize1('dog')
print(colorized_dog())                    # yellow dog
# () - означає виклик ф-ції
