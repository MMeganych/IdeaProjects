# Method Resolution Order (MRO)

#    A
#   /  \
#   B   C
#   \   /
#     D

class A:
    def some_method(self):
        print('Method of class A')


class B(A):
    def some_method(self):
        print('Method of class B')


class C(A):
    def some_method(self):
        print('Method of class C')


class D(B, C):
    def some_method(self):
        print('Method of class D')


# __mro__,mro(), help() - способи опреділити ієрархію методів класів

print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.mro())   # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
help(D)
# class D(B, C)
# |  Method resolution order:
# |      D
# |      B
# |      C
# |      A
# |      builtins.object
# |
# |  Methods defined here:
# |
# |  some_method(self)
# |
# |  ----------------------------------------------------------------------
# |  Data descriptors inherited from A:
# |
# |  __dict__
# |      dictionary for instance variables (if defined)
# |
# |  __weakref__
# |      list of weak references to the object (if defined)

some_object = D()
some_object.some_method()   # Method of class D


# якщо закоментувати метод some_method() в класі D, то тут відображується метод класу В
# Method of class B

# якщо закоментувати метод some_method() в класі B, то тут відображується метод класу C
# Method of class C

# якщо закоментувати метод some_method() в класі C, то тут відображується метод класу A
# Method of class A

#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)