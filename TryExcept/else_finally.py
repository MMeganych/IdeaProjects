# Якщо ми маэмо помилку - except блок спрацьовує, а else блок не спрацьовує
# Якщо ми не маэмо помилку - except блок не спрацьовує, а else блок спрацьовує
# Finally block, виконуэться в любому випадку

number = input('Enter some number: ')

try:
    print(int(number) / 2)   # 2.0
except:
    print('You have to enter a number')
else:
    print('Else block')

print('Code after error handling')

# Enter some number: hi
# You have to enter a number
# Code after error handling

# -------------------------------------

# Enter some number: 3
# 1.5
# Else block
# Code after error handling

# ---------------------------------------------------------
number = input('Enter some number: ')

try:
    print(int(number) / 2)   # 2.0
except:
    print('You have to enter a number')
else:
    print('Else block')
finally:
    print('Finally block')

print('Code after error handling')

# Enter some number: 3
# 1.5
# Else block
# Finally block
# Code after error handling

# -----------------------------------

# Enter some number: hi
# You have to enter a number
# Finally block
# Code after error handling

# ---------------------------------------------------------

while True:
    try:
        number = int(input('Enter some number: '))
        print(number / 2)
    except:
        print('You have to enter a number')
    else:
        print('Good job! This is a number!')
        break
    finally:
        print('Finally block')

print('Code after error handling')
# Enter some number: gggg
# You have to enter a number
# Finally block
#
# Enter some number: hhhh
# You have to enter a number
# Finally block
#
# Enter some number: 33
# 16.5
# Good job! This is a number!
# Finally block
# Code after error handling


def divide(x, y):
    return x / y


print(divide(4, 2))        # 2.0
print(divide(4, 0))        # ZeroDivisionError: division by zero
print(divide(4, 'w'))      # TypeError

# ------------------------------------------------------------------------------------------


def divide_2(x, y):
    try:
        print(x / y)
    except ZeroDivisionError:
        print('You can\'t divide by zero!')
    except TypeError:
        print('x and y must be numbers')
    else:
        print('x was divided by y')
    finally:
        print('Finally block')


print(divide_2(4, 2))      # 2.0
#                          # x has divided by y
#                          # None
#                          # Finally block

print(divide_2(4, 0))      # You can't divide by zero!
#                          # Finally block
#                          # None

print(divide_2(4, 'w'))    # x and y must be numbers
#                          # Finally block
#                          # None











