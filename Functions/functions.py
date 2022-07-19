# # build-in functions
# x = print('Hello!')
# y = set()
#
# print(type(x))
# print(type(y))
#
# # build-in methods
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)
# my_list.clear()
# print(my_list)

def print_greeting():
    '''
    Print 'Hello! text
    :return: None
    '''
    print('Hello!')
# call the function (виклик функцій)
print_greeting()
help(print_greeting) # викликати опис функції, функцію вписуємо без скобок
# print_greeting()
# Print 'Hello! text
# :return: None

def print_greeting_with_name(name = 'name'):
    '''
    :param name
    :return: None
    '''
    print('Hello ' + name + '!')

print(print_greeting_with_name('Jack'))    # Hello Jack!
help(print_greeting_with_name)
# print_greeting_with_name(name)
#     :param name
#     :return: None

def sum_of_two_numbers(a = 0, b = 0):
    '''
    
    :param a: The first addend
    :param b: The second addend
    :return: Sum of a and b
    '''
    return a + b
x = sum_of_two_numbers(1, 1)
print(x) # 2
help(sum_of_two_numbers)
# sum_of_two_numbers(a=0, b=0)
#     :param a: The first addend
#     :param b: The second addend
#     :return: Sum of a and b

def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False
print(is_hello_in_text('Say hello everyone'))  # True
print(is_hello_in_text('Say everyone'))  # False
print(is_hello_in_text('Hello everyone!'))  # False  (бо слово "Hello" написано з великої літери)
print(is_hello_in_text('Hello everyone!'))  # True (if 'hello' in text.lower():)

# простіший і коротший приклад.
# Ми знаємо, що оператор "in" повертає значення True або False, в залежності від того чи лежить якийсь елемент
# в послідовності або ні.

def is_hello_in_text(text):
    return 'hello' in text.lower()


print(is_hello_in_text('Hello everyone!'))  # True


def is_string_in_text(string, text):
    return string in text


print(is_string_in_text('he', 'The apple'))  # True (шукатиме строку 'he' в тексті 'The apple')
print(is_string_in_text('heу', 'The apple')) # False (шукатиме строку 'hey' в тексті 'The apple')


def greeeting_depens_on_gender(name, gender):
    if gender == 'male':
        print('Hello ' + name + '! You look great!')
        return gender
    elif gender == 'female':
        print('Hello ' + name + '! You are so nice!')
        return gender
    else:
        print('Hello ' + name + '! I\'ve never seen the creature like you!')
        return gender


returned_value = greeeting_depens_on_gender('Jack', 'male')    # Hello Jack! You look great!
returned_value = greeeting_depens_on_gender('Jane', 'female')  # Hello Jane! You are so nice!
returned_value = greeeting_depens_on_gender('Ja', 'cmale')     # Hello Ja! I've never seen the creature like you!

def cat_voice():
    '''
    Print 'Meow!' text
    :return: None
    '''
    print('Meow!')


def dog_voice():
    '''
    Print 'Woof!' text
    :return: None
    '''
    print('Woof!')


print(dog_voice())
print(cat_voice())


def cat_voice():
   return print(' Meow!' * 2)

print(cat_voice())

def dog_voice():
   return print(' Woof!' * 2)

print(dog_voice())


def get_voice(text):
    return text + '!'


print(get_voice('Hello'))


def odd_sequence(a, b):
    number_list = [num for num in range(a, b + 1) if num % 2 != 0]
    return print(number_list)


odd_sequence(7, 102)


def odd_sequence(a, b):
    number_list = []
    for num in range(a, b + 1):
        if num % 2 != 0:
            number_list.append(num)
    return print(number_list)


odd_sequence(14, 95)