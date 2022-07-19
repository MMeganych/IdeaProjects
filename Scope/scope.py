pi = 'outer pi variable'

def print_pi():
    pi = 'inner pi variable'
    print(pi)

print_pi()           # inner pi variable
print(pi)            # outer pi variable

# Local Scope

pi = 'global pi variable'
def inner():
    pi = 'inner pi variable'
    print(pi)

inner()      # inner pi variable


pi = 'global pi variable'
def inner():
    print(pi)

inner()      # global pi variable


# Global Scope

pi = 'global pi variable'
def inner():
    pi = 'inner pi variable'
    print(pi)

inner()      # inner pi variable
print(pi)    # global pi variable


# Enclosed Scope

pi = 'global pi variable'

def outer():
    pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        nonlocal pi   # - йде звернення із внутрішньої ф-ції в перемінну зовнішньої ф-ції
        print(pi)
    inner()

outer()               # outer pi variable
print(pi)             # global pi variable


pi = 'global pi variable'

def outer():
    pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        nonlocal pi        # змінення значення ,рі, на 'new value' в зовн. ф-ції
        pi = 'new value'
        print(pi)
    inner()

outer()                  # new value
print(pi)                # global pi variable


pi = 'global pi variable'

def outer():
    pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        global pi        # змінення значення ,рі, на 'new value' в глобальній перемінній ,рі,
        pi = 'new value'
        print(pi)
    inner()

outer()                  # new value
print(pi)                # new value


# Built-in Scope
from math import pi

# pi = 'global pi variable'

def outer():
    # pi = 'outer pi variable'
    def inner():
        # pi = 'inner pi variable'
        print(pi)
    inner()

outer()              # 3.141592653589793 (число РІ)


