# x = 1
# y = 2
# print(x > 1)
# print(y > 1)
#
#  # and, or, not
# print(x > 1 and y > 1)  # False
# print(x > 1 or y > 1)   # True
# print(not x > 1)        # True
# print(not y > 1)        # False

print(True and True)      # True
print(True or True)       # True
print(not True)           # False

print(False and False)    # False
print(False or False)     # False
print(not False)          # True

print(True and False)    # False
print(True or False)     # True

name = 'John'
age = 21
is_married = False

if age > 18 and is_married == False:
    print('Hi {}! You can find a girl of you dream here!'.format(name))
    #Hi John! You can find a girl of you dream here!

